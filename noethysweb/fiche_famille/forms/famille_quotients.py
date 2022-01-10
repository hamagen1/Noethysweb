# -*- coding: utf-8 -*-
#  Copyright (c) 2019-2021 Ivan LUCAS.
#  Noethysweb, application de gestion multi-activités.
#  Distribué sous licence GNU GPL.

from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Hidden, Div, HTML, Fieldset, ButtonHolder
from crispy_forms.bootstrap import Field, StrictButton, PrependedText
from core.forms.base import FormulaireBase
from core.utils.utils_commandes import Commandes
from core.models import Famille, Quotient
from core.widgets import DatePickerWidget
from core.utils import utils_preferences


class Formulaire(FormulaireBase, ModelForm):

    class Meta:
        model = Quotient
        fields = "__all__"
        widgets = {
            'observations': forms.Textarea(attrs={'rows': 4}),
            'date_debut': DatePickerWidget(),
            'date_fin': DatePickerWidget(),
        }

    def __init__(self, *args, **kwargs):
        idfamille = kwargs.pop("idfamille")
        super(Formulaire, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'famille_quotients_form'
        self.helper.form_method = 'post'

        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-10'

        # Définit la famille associée
        famille = Famille.objects.select_related("caisse", "allocataire").get(pk=idfamille)

        # Si ajout : insertion des valeurs du précédent quotient saisi
        if not self.instance.pk:
            dernier_quotient = Quotient.objects.last()
            if dernier_quotient:
                self.fields["date_debut"].initial = dernier_quotient.date_debut
                self.fields["date_fin"].initial = dernier_quotient.date_fin
                self.fields["type_quotient"].initial = dernier_quotient.type_quotient

        # Affichage
        self.helper.layout = Layout(
            Commandes(annuler_url="{{ view.get_success_url }}"),
            Hidden('famille', value=idfamille),
            Fieldset("Période de validité",
                Field('date_debut'),
                Field('date_fin'),
            ),
            Fieldset("Paramètres",
                Field('type_quotient'),
                PrependedText('quotient', utils_preferences.Get_symbole_monnaie()),
                PrependedText('revenu', utils_preferences.Get_symbole_monnaie()),
                Field('observations'),
            ),
            Fieldset("Document numérisé",
                Field('document'),
            ),
        )

        # Affichage des informations de la caisse
        if not self.instance.pk:
            self.helper.layout.insert(1,
                Fieldset("Rappel des données allocataire",
                    Div(
                        HTML("""
                        <span>Caisse : %s</span>
                        <span class="ml-5">Allocataire : %s</span>
                        <span class="ml-5">N° allocataire : %s</span>
                        """ % (famille.caisse.nom or "Inconnue", famille.allocataire or "Inconnu", famille.num_allocataire or "Inconnu")),
                        css_class="alert alert-light text-center"
                    ),
                ),
            )

    def clean(self):
        if self.cleaned_data["date_debut"] > self.cleaned_data["date_fin"]:
            self.add_error('date_fin', "La date de fin doit être supérieure à la date de début")
            return

        return self.cleaned_data
