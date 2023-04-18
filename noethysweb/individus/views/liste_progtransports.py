# -*- coding: utf-8 -*-
#  Copyright (c) 2019-2021 Ivan LUCAS.
#  Noethysweb, application de gestion multi-activités.
#  Distribué sous licence GNU GPL.

from django.urls import reverse_lazy, reverse
from core.views.mydatatableview import MyDatatable, columns, helpers
from core.views import crud
from core.models import Transport
from fiche_individu.forms.individu_transport import Formulaire


class Page(crud.Page):
    model = Transport
    url_liste = "progtransports_liste"
    url_modifier = "progtransports_modifier"
    url_supprimer = "progtransports_supprimer"
    description_liste = "Voici ci-dessous la liste des programmations de transports."
    description_saisie = "Saisissez toutes les informations concernant la programmation de transports et cliquez sur le bouton Enregistrer."
    objet_singulier = "une programmation de transports"
    objet_pluriel = "des programmations de transports"


class Liste(Page, crud.Liste):
    model = Transport

    def get_queryset(self):
        return Transport.objects.filter(self.Get_filtres("Q"), mode="PROG")

    def get_context_data(self, **kwargs):
        context = super(Liste, self).get_context_data(**kwargs)
        context['impression_introduction'] = ""
        context['impression_conclusion'] = ""
        context['afficher_menu_brothers'] = True
        return context

    class datatable_class(MyDatatable):
        filtres = ["idtransport", "categorie", "date_debut", "date_fin", "origine", "destination", "individu__nom", "individu__prenom"]
        categorie = columns.TextColumn("Catégorie", sources="categorie", processor="Get_categorie")
        origine = columns.TextColumn("Origine", sources=["depart_lieu", "depart_arret"], processor="Get_origine")
        destination = columns.TextColumn("Destination", sources=["arrivee_lieu", "arrivee_arret"], processor="Get_destination")
        nom = columns.TextColumn("Nom", sources=["individu__nom"])
        prenom = columns.TextColumn("Prénom", sources=["individu__prenom"])
        actions = columns.TextColumn("Actions", sources=None, processor='Get_actions_standard')

        class Meta:
            structure_template = MyDatatable.structure_template
            columns = ["idtransport", "nom", "prenom", "categorie", "date_debut", "date_fin", "origine", "destination"]
            processors = {
                "date_debut": helpers.format_date("%d/%m/%Y"),
                "date_fin": helpers.format_date("%d/%m/%Y"),
            }
            ordering = ["idtransport"]

        def Get_categorie(self, instance, **kwargs):
            return instance.get_categorie_display()

        def Get_origine(self, instance, **kwargs):
            if instance.depart_lieu: return instance.depart_lieu.nom
            if instance.depart_arret: return instance.depart_arret.nom
            if instance.depart_localisation: return instance.depart_localisation
            return ""

        def Get_destination(self, instance, **kwargs):
            if instance.arrivee_lieu: return instance.arrivee_lieu.nom
            if instance.arrivee_arret: return instance.arrivee_arret.nom
            if instance.arrivee_localisation: return instance.arrivee_localisation
            return ""


class Ajouter(Page, crud.Ajouter):
    form_class = Formulaire


class Modifier(Page, crud.Modifier):
    form_class = Formulaire


class Supprimer(Page, crud.Supprimer):
    pass
