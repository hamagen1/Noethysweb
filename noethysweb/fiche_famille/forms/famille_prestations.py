# -*- coding: utf-8 -*-
#  Copyright (c) 2019-2021 Ivan LUCAS.
#  Noethysweb, application de gestion multi-activités.
#  Distribué sous licence GNU GPL.

import datetime
from django import forms
from django.forms import ModelForm
from core.forms.base import FormulaireBase
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Hidden, HTML, Fieldset, Div
from crispy_forms.bootstrap import Field, PrependedText
from core.utils.utils_commandes import Commandes
from core.models import Famille, Prestation, Deduction, Individu, Rattachement, Inscription, Activite
from core.widgets import DatePickerWidget, Formset
from django.forms.models import inlineformset_factory, BaseInlineFormSet
from core.utils import utils_preferences
from fiche_famille.widgets import Facture_prestation



class DeductionForm(forms.ModelForm):

    class Meta:
        model = Deduction
        exclude = []

    def __init__(self, *args, **kwargs):
        super(DeductionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.form_class = "formset_deductions"

    def clean(self):
        # if self.cleaned_data.get('DELETE') == False:
        #
        #     # Vérifie qu'au moins une unité a été saisie
        #     if len(self.cleaned_data["unites"]) == 0:
        #         raise forms.ValidationError('Vous devez sélectionner au moins une unité')
        #
        return self.cleaned_data


class BaseDeductionFormSet(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        super(BaseDeductionFormSet, self).__init__(*args, **kwargs)

    def clean(self):
        for form in self.forms:
            if self._should_delete_form(form) == False:

                # Vérification de la validité de la ligne
                if form.is_valid() == False or len(form.cleaned_data) == 0:
                    for field, erreur in form.errors.as_data().items():
                        message = erreur[0].message
                        form.add_error(field, message)
                        return



FORMSET_DEDUCTIONS = inlineformset_factory(Prestation, Deduction, form=DeductionForm, fk_name="prestation", formset=BaseDeductionFormSet,
                                            fields=["montant", "label"], extra=1, min_num=0,
                                            can_delete=True, validate_max=True, can_order=False)



class Formulaire(FormulaireBase, ModelForm):
    quantite = forms.IntegerField(label="Quantité", initial=1, min_value=1, required=True)
    montant_unitaire = forms.DecimalField(label="Montant unitaire", max_digits=6, decimal_places=2, initial=0.0, required=True)

    class Meta:
        model = Prestation
        fields = "__all__"
        widgets = {
            "date": DatePickerWidget(),
            "facture": Facture_prestation(),
        }
        labels = {
            "montant_initial": "Montant initial",
            "montant": "Montant final",
        }
        help_texts = {
            "montant_initial": "Le montant initial est égal à quantité x montant unitaire.",
            "montant": "Le montant final est égal à montant initial - total des déductions.",
        }

    def __init__(self, *args, **kwargs):
        idfamille = kwargs.pop("idfamille")
        super(Formulaire, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'famille_prestations_form'
        self.helper.form_method = 'post'

        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-10'

        # Date
        if not self.instance.pk:
            self.fields["date"].initial = datetime.date.today()

        # Individu
        rattachements = Rattachement.objects.select_related("individu").filter(famille_id=idfamille).order_by("individu__nom", "individu__prenom")
        self.fields["individu"].choices = [(None, "---------")] + [(rattachement.individu.idindividu, rattachement.individu) for rattachement in rattachements]

        # Activité
        activites = {inscription.activite_id: inscription.activite.nom for inscription in Inscription.objects.select_related("activite").filter(famille_id=idfamille)}
        self.fields["activite"].choices = [(None, "---------")] + [(idactivite, nom_activite) for idactivite, nom_activite in activites.items()]

        # Si prestation facturée
        if self.instance.facture:
            for champ in ("date", "categorie", "individu", "activite", "categorie_tarif", "tarif", "quantite", "montant_unitaire", "montant_initial", "montant", "tva"):
                self.fields[champ].disabled = True
                self.fields[champ].help_text = "Ce champ n'est pas modifiable car la prestation est déjà facturée."

        # Affichage
        self.helper.layout = Layout(
            Commandes(annuler_url="{{ view.get_success_url }}"),
            Hidden('famille', value=idfamille, id="id_famille"),
            Fieldset("Généralités",
                Field('date'),
                Field('categorie'),
                Field('label'),
                Field('individu'),
            ),
            Fieldset("Activité",
                Field('activite'),
                Field('categorie_tarif'),
                Field('tarif'),
                id="fieldset_activite",
            ),
            Fieldset("Tarification",
                PrependedText('tva', '%'),
                PrependedText('montant_unitaire', utils_preferences.Get_symbole_monnaie()),
                Field('quantite'),
                PrependedText('montant_initial', utils_preferences.Get_symbole_monnaie()),
                PrependedText('montant', utils_preferences.Get_symbole_monnaie()),
            ),
            Fieldset("Comptabilité",
                Field('code_compta'),
                Field('code_produit_local'),
            ),
            Fieldset("Facturation",
                Field('facture'),
            ),
            Fieldset("Déductions",
                Div(
                    Div(
                        HTML("<label class='col-form-label col-md-2 requiredField'><b></b></label>"),
                        Div(
                            Formset("formset_combi"),
                            css_class="controls col-md-10"
                        ),
                        css_class="form-group row"
                    ),
                ),
            ),
            HTML(EXTRA_HTML),
        )

    def clean(self):
        return self.cleaned_data

EXTRA_HTML = """
<script>

// Sur sélection de l'individu
function On_selection_individu() {
    $('#fieldset_activite').hide();
    if ($("#id_individu").val()) {
        $('#fieldset_activite').show();
    };
    var idindividu = $("#id_individu").val();
    var idfamille = $("#id_famille").val();
    var idactivite = $("#id_activite").val();
    $.ajax({ 
        type: "POST",
        url: "{% url 'ajax_get_activites_prestation' %}",
        data: {
            'idindividu': idindividu,
            'idfamille': idfamille,
        },
        success: function (data) { 
            $("#id_activite").html(data); 
            $("#id_activite").val(idactivite);
            if (data == '') {
                $("#fieldset_activite").hide()
            } else {
                $("#fieldset_activite").show()
            }
            On_change_activite();
        }
    });
}
$(document).ready(function() {
    $('#id_individu').on('change', On_selection_individu);
    On_selection_individu.call($('#id_individu').get(0));
});


// Actualise la liste des catégories de tarifs
function On_change_activite() {
    var idactivite = $("#id_activite").val();
    var idcategorie_tarif = $("#id_categorie_tarif").val();
    $.ajax({ 
        type: "POST",
        url: "{% url 'ajax_get_categories_tarifs' %}",
        data: {'idactivite': idactivite},
        success: function (data) { 
            $("#id_categorie_tarif").html(data); 
            $("#id_categorie_tarif").val(idcategorie_tarif);
            if (data == '') {
                $("#div_id_categorie_tarif").hide()
            } else {
                $("#div_id_categorie_tarif").show()
            }
            On_change_categorie_tarif();
        }
    });
};
$(document).ready(function() {
    $('#id_activite').change(On_change_activite);
    On_change_activite.call($('#id_activite').get(0));
});


// Actualise la liste des tarifs
function On_change_categorie_tarif() {
    var idactivite = $("#id_activite").val();
    var idcategorie_tarif = $("#id_categorie_tarif").val();
    var idtarif = $("#id_tarif").val();
    $.ajax({ 
        type: "POST",
        url: "{% url 'ajax_get_tarifs_prestation' %}",
        data: {
            'idactivite': idactivite, 
            'idcategorie_tarif': idcategorie_tarif
        },
        success: function (data) { 
            $("#id_tarif").html(data); 
            $("#id_tarif").val(idtarif);
            if (data == '') {
                $("#div_id_tarif").hide()
            } else {
                $("#div_id_tarif").show()
            }
        }
    });
};
$(document).ready(function() {
    $('#id_categorie_tarif').change(On_change_categorie_tarif);
    On_change_categorie_tarif.call($('#id_categorie_tarif').get(0));
});

// Calcul du total des déductions

function formset_apres_ajout(row) {
    init_calcul_montant_final();
};
    
function formset_apres_suppression(row) {
    init_calcul_montant_final();
};

function init_calcul_montant_final() {
    $("input[name*='-montant']").on('input', function() {
        calcul_montant_final();
    });
    calcul_montant_final();
};

function calcul_montant_final() {

    // Calcule le total des déductions
    var total_deductions = 0.0;
    $("input[name*='-montant']").filter(':visible').each(function(){
        var montant = parseFloat($(this).val());
        if (montant){
            total_deductions = total_deductions + montant;
        };
    });
    
    // Calcule le montant initial
    var quantite = $("#id_quantite").val();
    var montant_unitaire = $("#id_montant_unitaire").val();
    var montant_initial = montant_unitaire * quantite;
    $("#id_montant_initial").val(montant_initial.toFixed(2));
    
    // Affiche le montant final
    var montant_final = montant_initial - total_deductions;
    $("#id_montant").val(montant_final.toFixed(2));
    
};

$(document).ready(function() {
    // Calcule le montant unitaire
    var quantite = $("#id_quantite").val();
    var montant_initial = $("#id_montant_initial").val();
    var montant_unitaire = montant_initial / quantite;
    $("#id_montant_unitaire").val(montant_unitaire.toFixed(2));
    
    // Calcule le montant final
    $("#id_montant_unitaire, #id_montant_initial, #id_quantite").on('input', function() {
        calcul_montant_final();
    });
    init_calcul_montant_final();
    
    // Désactive le montant initial et le montant final
    $("#id_montant_initial").prop('readonly', 'true');
    $("#id_montant").prop('readonly', 'true');

    // Désactive les déductions si prestation facturée
    if ($("#id_facture").val()) {
        $("input[name*='deduction_set']").prop('readonly', 'true');
        $(".delete-row-deduction_set").prop('hidden', true);
        $(".add-row-deduction_set").prop('hidden', true);
    };
        
});

</script>
"""
