# -*- coding: utf-8 -*-
#  Copyright (c) 2019-2021 Ivan LUCAS.
#  Noethysweb, application de gestion multi-activités.
#  Distribué sous licence GNU GPL.

from django import forms
from core.forms.select2 import Select2MultipleWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import Field
from core.widgets import DateRangePickerWidget
from core.utils.utils_commandes import Commandes
from core.forms.base import FormulaireBase
from core.models import ModelePlanningCollaborateur


class Formulaire(FormulaireBase, forms.Form):
    periode = forms.CharField(label="Période", required=True, widget=DateRangePickerWidget(), help_text="Sélectionnez la période sur laquelle appliquer les modèles.")
    modeles = forms.ModelMultipleChoiceField(label="Modèles", required=True, widget=Select2MultipleWidget({"data-minimum-input-length": 0}),
                                             queryset=ModelePlanningCollaborateur.objects.none(), help_text="Sélectionnez un ou plusieurs modèles de planning à appliquer.")

    def __init__(self, *args, **kwargs):
        super(Formulaire, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-10'

        self.fields["modeles"].queryset = ModelePlanningCollaborateur.objects.all().order_by("nom")

        self.helper.layout = Layout(
            Commandes(enregistrer_label="<i class='fa fa-check margin-r-5'></i>Appliquer", ajouter=False, annuler_url="{% url 'collaborateur_evenements_liste' idcollaborateur=idcollaborateur %}"),
            Field("periode"),
            Field("modeles"),
        )
