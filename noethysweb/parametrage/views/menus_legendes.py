# -*- coding: utf-8 -*-

#  Copyright (c) 2019-2021 Ivan LUCAS.
#  Noethysweb, application de gestion multi-activités.
#  Distribué sous licence GNU GPL.

from django.urls import reverse_lazy, reverse
from core.views.mydatatableview import MyDatatable, columns, helpers
from core.views import crud
from core.models import MenuLegende
from parametrage.forms.menus_legendes import Formulaire


class Page(crud.Page):
    model = MenuLegende
    url_liste = "menus_legendes_liste"
    url_ajouter = "menus_legendes_ajouter"
    url_modifier = "menus_legendes_modifier"
    url_supprimer = "menus_legendes_supprimer"
    description_liste = "Voici ci-dessous la liste des légendes de menus."
    description_saisie = "Saisissez toutes les informations concernant la légende de menu à saisir et cliquez sur le bouton Enregistrer."
    objet_singulier = "une légende de menu"
    objet_pluriel = "des légendes de menus"
    boutons_liste = [
        {"label": "Ajouter", "classe": "btn btn-success", "href": reverse_lazy(url_ajouter), "icone": "fa fa-plus"},
    ]


class Liste(Page, crud.Liste):
    model = MenuLegende

    def get_queryset(self):
        return MenuLegende.objects.filter(self.Get_filtres("Q"))

    def get_context_data(self, **kwargs):
        context = super(Liste, self).get_context_data(**kwargs)
        context['impression_introduction'] = ""
        context['impression_conclusion'] = ""
        context['afficher_menu_brothers'] = True
        return context

    class datatable_class(MyDatatable):
        filtres = ["idlegende", "nom"]

        actions = columns.TextColumn("Actions", sources=None, processor='Get_actions_standard')

        class Meta:
            structure_template = MyDatatable.structure_template
            columns = ["idlegende", "nom"]
            #hidden_columns = = ["idlegende"]
            ordering = ["nom"]


class Ajouter(Page, crud.Ajouter):
    form_class = Formulaire

class Modifier(Page, crud.Modifier):
    form_class = Formulaire

class Supprimer(Page, crud.Supprimer):
    pass
