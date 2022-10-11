# -*- coding: utf-8 -*-
#  Copyright (c) 2019-2021 Ivan LUCAS.
#  Noethysweb, application de gestion multi-activités.
#  Distribué sous licence GNU GPL.

import datetime, logging
logger = logging.getLogger(__name__)
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.db.models.functions import Concat
from django.db.models import Count, F, CharField, Value, Q, Min, Max
from core.views.base import CustomView
from core.models import Consommation, Prestation
from outils.forms.correcteur import Formulaire


class Anomalie():
    def __init__(self, idcategorie=None, idfamille=None, idindividu=None, idactivite=None, date_min=None, date_max=None, label="", corrigeable=True, importation=None):
        self.idcategorie = idcategorie
        self.idfamille = idfamille
        self.idindividu = idindividu
        self.idactivite = idactivite
        self.date_min = date_min
        self.date_max = date_max
        self.label = label
        self.corrigeable = corrigeable
        self.importation = importation

        if self.importation:
            self.Importation()

        # Génération d'un pk basé sur les données
        self.pk = "idcategorie=%s__idfamille=%d__idindividu=%d__idactivite=%d__date_min=%s__date_max=%s" % (self.idcategorie, self.idfamille or 0, self.idindividu or 0, self.idactivite or 0, self.date_min, self.date_max)

    def Importation(self):
        for item in self.importation.split("__"):
            code, valeur = item.split("=")
            if code in ("idfamille", "idindividu", "idactivite"):
                valeur = int(valeur)
            if code in ("date_min", "date_max") and valeur != "None":
                valeur = datetime.datetime.strptime(valeur, "%Y-%m-%d").date()
            setattr(self, code, valeur)


class View(CustomView, TemplateView):
    form_class = Formulaire
    template_name = "core/crud/edit.html"
    menu_code = "correcteur"

    def get_context_data(self, **kwargs):
        context = super(View, self).get_context_data(**kwargs)
        context['page_titre'] = "Correcteur d'anomalies"
        context['box_titre'] = ""
        context['box_introduction'] = "Voici la liste des anomalies détectées dans les données."
        context['form'] = Formulaire(request=self.request, anomalies=self.Get_anomalies())
        return context

    def Get_anomalies(self):
        data = {}

        # Recherche les doublons dans les consommations (pour un individu sur une même date avec la même unité)
        qs = Consommation.objects.select_related("individu", "inscription").annotate(doublon_id=Concat(F("individu_id"), Value("_"), F("inscription_id"), Value("_"), F("unite_id"), Value("_"), F("date"), Value("_"), F("evenement_id"), output_field=CharField()))
        doublons = qs.values("individu__nom", "individu__prenom", "individu__pk", "inscription__famille_id", "activite__pk", "date", "doublon_id").annotate(nbre_doublons=Count("doublon_id")).filter(nbre_doublons__gt=1)
        data["Doublons de consommations"] = [Anomalie(
            label="%s %s : %d doublons le %s." % (d["individu__nom"], d["individu__prenom"], d["nbre_doublons"], d["date"]),
            idcategorie="doublons_consommations", idfamille=d["inscription__famille_id"], idindividu=d["individu__pk"], idactivite=d["activite__pk"], date_min=d["date"], date_max=d["date"],
            corrigeable=False)
            for d in doublons]

        # Recherche les doublons dans les prestations (pour un individu sur une même date avec le même tarif de prestation)
        qs = Prestation.objects.select_related("individu").annotate(doublon_id=Concat(F("individu_id"), Value("_"), F("famille_id"), Value("_"), F("tarif_id"), Value("_"), F("date"), output_field=CharField()))
        doublons = qs.values("individu__nom", "individu__prenom", "date", "individu__pk", "famille__pk", "activite__pk", "doublon_id").annotate(nbre_doublons=Count("doublon_id")).filter(nbre_doublons__gt=1)
        data["Doublons de prestations"] = [Anomalie(
            label="%s %s : %d doublons le %s." % (d["individu__nom"], d["individu__prenom"], d["nbre_doublons"], d["date"]),
            idcategorie="doublons_prestations", idfamille=d["famille__pk"], idindividu=d["individu__pk"], idactivite=d["activite__pk"], date_min=d["date"], date_max=d["date"])
            for d in doublons]

        # Recherche les consommations gratuites
        resultats = Consommation.objects.values("activite__nom").filter(prestation_id=None, etat__in=("reservation", "present", "absenti")).annotate(nbre=Count("pk"), min_date=Min("date"), max_date=Max("date"))
        data["Consommations gratuites"] = [Anomalie(
            label="%s : %s consommations (Du %s au %s)." % (r["activite__nom"], r["nbre"], r["min_date"].strftime("%d/%m/%Y"), r["max_date"].strftime("%d/%m/%Y")),
            idcategorie="conso_gratuites", corrigeable=False)
            for r in resultats]

        # Recherche les prestations sans consommations associées
        resultats = Prestation.objects.select_related("individu").values("individu__nom", "individu__prenom", "individu__pk", "famille__pk", "activite__pk", "label").filter(consommation__isnull=True, categorie="consommation").annotate(nbre=Count("pk"), min_date=Min("date"), max_date=Max("date")).order_by("individu__nom", "individu__prenom")
        data["Prestations sans consommations associées"] = [Anomalie(
            label="%s %s : %s %s (Du %s au %s)." % (r["individu__nom"], r["individu__prenom"], r["nbre"], r["label"], r["min_date"].strftime("%d/%m/%Y"), r["max_date"].strftime("%d/%m/%Y")),
            idcategorie="presta_sans_conso", idfamille=r["famille__pk"], idindividu=r["individu__pk"], idactivite=r["activite__pk"], date_min=r["min_date"], date_max=r["max_date"])
            for r in resultats]

        return data

    def post(self, request, **kwargs):
        anomalies = request.POST.getlist("anomalies")

        # Importation de la grille virtuelle
        from consommations.utils.utils_grille_virtuelle import Grille_virtuelle

        # Correction des anomalies
        for pk in anomalies:
            anomalie = Anomalie(importation=pk)

            # Recalcul de prestations dans la grille virtuelle
            if anomalie.idcategorie in ("doublons_prestations", "presta_sans_conso"):
                logger.debug("Tentative de correction de l'anomalie : idfamille=%d, idindividu=%d, idactivite=%d, date_min=%s, date_max=%s." % (anomalie.idfamille, anomalie.idindividu, anomalie.idactivite, anomalie.date_min, anomalie.date_max))
                grille = Grille_virtuelle(request=request, idfamille=anomalie.idfamille, idindividu=anomalie.idindividu, idactivite=anomalie.idactivite, date_min=anomalie.date_min, date_max=anomalie.date_max)
                grille.Recalculer_tout()
                grille.Enregistrer()

        return HttpResponseRedirect(reverse_lazy("correcteur"))
