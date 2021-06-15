# -*- coding: utf-8 -*-
#  Copyright (c) 2019-2021 Ivan LUCAS.
#  Noethysweb, application de gestion multi-activités.
#  Distribué sous licence GNU GPL.

from django.urls import reverse_lazy
from fiche_individu.forms.individu_appliquer_forfait_date import Formulaire
from fiche_individu.views.individu import Onglet
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import messages
from individus.utils import utils_forfaits
from core.models import Inscription


class View(Onglet, TemplateView):
    template_name = "fiche_individu/individu_edit.html"

    def get_context_data(self, **kwargs):
        context = super(View, self).get_context_data(**kwargs)
        context['box_titre'] = "Appliquer un forfait daté"
        context['box_introduction'] = "Cochez un ou plusieurs forfaits datés et cliquez sur le bouton Appliquer."
        context['onglet_actif'] = "inscriptions"
        if "form" in kwargs:
            context['form'] = Formulaire(self.request.POST.copy(), idfamille=self.kwargs['idfamille'], idindividu=self.kwargs['idindividu'], request=self.request)
        else:
            context['form'] = Formulaire(idfamille=self.kwargs['idfamille'], idindividu=self.kwargs['idindividu'], request=self.request)
        return context

    def post(self, request, **kwargs):
        # Validation du form
        form = Formulaire(request.POST, idfamille=self.kwargs['idfamille'], idindividu=self.kwargs['idindividu'], request=self.request)
        if form.is_valid() == False:
            return self.render_to_response(self.get_context_data(form=form))

        # Si coche sur masquer_forfaits_obsoletes
        if form.cleaned_data["action"] == "afficher_forfaits_obsoletes":
            return self.render_to_response(self.get_context_data(form=form))

        # Vérifie qu'au moins un forfait est coché
        forfaits = form.cleaned_data.get("forfaits")
        if not forfaits:
            messages.add_message(request, messages.ERROR, "Veuillez cocher au moins un forfait à appliquer")
            return self.render_to_response(self.get_context_data(form=form))

        # Application des forfaits
        liste_tarifs = [int(idtarif) for idtarif in forfaits.split(";")]
        activites = [inscription.activite_id for inscription in Inscription.objects.filter(famille=self.Get_idfamille(), individu=self.Get_idindividu())]
        f = utils_forfaits.Forfaits(famille=self.Get_idfamille(), activites=activites, individus=[self.Get_idindividu()], saisie_manuelle=True, saisie_auto=False)
        for idtarif in liste_tarifs:
            f.Applique_forfait(request=self.request, mode_inscription=False, selection_tarif=idtarif, selection_activite=activites)

        return HttpResponseRedirect(reverse_lazy("individu_inscriptions_liste", args=(self.kwargs['idfamille'], self.kwargs['idindividu'])))
