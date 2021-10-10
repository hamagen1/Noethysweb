# -*- coding: utf-8 -*-
#  Copyright (c) 2019-2021 Ivan LUCAS.
#  Noethysweb, application de gestion multi-activités.
#  Distribué sous licence GNU GPL.

from django.urls import reverse_lazy
from portail.views.fiche import Onglet, ConsulterBase
from portail.forms.individu_maladies import Formulaire


class Consulter(Onglet, ConsulterBase):
    form_class = Formulaire
    template_name = "portail/fiche_edit.html"
    mode = "CONSULTATION"
    onglet_actif = "individu_maladies"
    categorie = "individu_maladies"
    titre_historique = "Modifier les maladies"

    def get_context_data(self, **kwargs):
        context = super(Consulter, self).get_context_data(**kwargs)
        context['box_titre'] = "Maladies"
        context['box_introduction'] = "Cliquez sur le bouton Modifier au bas de la page pour modifier une des informations ci-dessous."
        context['onglet_actif'] = self.onglet_actif
        return context

    def get_object(self):
        return self.get_individu()



class Modifier(Consulter):
    mode = "EDITION"

    def get_context_data(self, **kwargs):
        context = super(Modifier, self).get_context_data(**kwargs)
        context['box_introduction'] = "Sélectionnez une ou plusieurs maladies dans le champ ci-dessous et cliquez sur le bouton Enregistrer."
        if not self.get_dict_onglet_actif().validation_auto:
            context['box_introduction'] += " Ces informations devront être validées par l'administrateur de l'application."
        return context

    def get_success_url(self):
        return reverse_lazy("portail_individu_maladies", kwargs={'idrattachement': self.kwargs['idrattachement']})
