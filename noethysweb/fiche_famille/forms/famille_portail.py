# -*- coding: utf-8 -*-
#  Copyright (c) 2019-2021 Ivan LUCAS.
#  Noethysweb, application de gestion multi-activités.
#  Distribué sous licence GNU GPL.

from django import forms
from django.forms import ModelForm
from core.forms.base import FormulaireBase
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Hidden, Submit, HTML, Row, Column, Fieldset, Div, ButtonHolder
from crispy_forms.bootstrap import Field, StrictButton
from core.utils.utils_commandes import Commandes
from core.models import Famille
from fiche_famille.widgets import Internet_identifiant, Internet_mdp


class Formulaire(FormulaireBase, ModelForm):
    internet_identifiant = forms.CharField(label="Identifiant", required=False, widget=Internet_identifiant())
    internet_mdp = forms.CharField(label="Mot de passe", required=False, widget=Internet_mdp(), help_text="Des étoiles ***** apparaissent lorsque le mot de passe a été personnalisé par l'utilisateur lors de la première connexion au portail. Dans ce cas, il vous est impossible de récupérer le mot de passe personnalisé, vous devez en générer un nouveau.")

    class Meta:
        model = Famille
        fields = ["internet_actif", "internet_identifiant", "internet_mdp", "internet_categorie"]
        help_texts = {
            "internet_categorie": "Les catégories permettent par exemple d'attribuer des périodes de réservations à certains comptes internet uniquement."
        }

    def __init__(self, *args, **kwargs):
        idfamille = kwargs.pop("idfamille")
        if "instance" not in kwargs:
            self.instance = Famille.objects.get(pk=idfamille)
        super(Formulaire, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'famille_portail_form'
        self.helper.form_method = 'post'

        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-10'

        # Création des boutons de commande
        autres_commandes = [HTML("""<a type='button' class='btn btn-default' title="Envoyer les codes par Email" onclick="impression_pdf()"><i class="fa fa-send-o margin-r-5"></i>Envoyer les codes par email</a> """)]
        if self.mode == "CONSULTATION":
            commandes = Commandes(modifier_url="famille_portail_modifier", modifier_args="idfamille=idfamille", modifier=True, enregistrer=False, annuler=False, ajouter=False, autres_commandes=autres_commandes)
            self.Set_mode_consultation()
        else:
            commandes = Commandes(annuler_url="{% url 'famille_portail' idfamille=idfamille %}", ajouter=False, autres_commandes=autres_commandes)

        # Affichage
        self.helper.layout = Layout(
            commandes,
            Hidden("idfamille", value=idfamille),
            Fieldset("Activation",
                Field("internet_actif"),
            ),
            Fieldset("Codes d'accès",
                Field("internet_identifiant"),
                Field("internet_mdp"),
            ),
            Fieldset("Options",
                Field("internet_categorie"),
            ),
            HTML(EXTRA_HTML),
        )


EXTRA_HTML = """

<script>

    function regenerer_identifiant() {
        $.ajax({
            type: "POST",
            url: "{% url 'ajax_regenerer_identifiant' %}",
            data: {
                idfamille: $('[name=idfamille]').val(),
                csrfmiddlewaretoken: "{{ csrf_token }}",
            },
            success: function (data) {
                $('#id_internet_identifiant').val(data.identifiant);
            },
            error: function (data) {
                toastr.error(data.responseJSON.erreur);
            }
        });
    };

    function regenerer_mdp() {
        $.ajax({
            type: "POST",
            url: "{% url 'ajax_regenerer_mdp' %}",
            data: {
                idfamille: $('[name=idfamille]').val(),
                csrfmiddlewaretoken: "{{ csrf_token }}",
            },
            success: function (data) {
                $('#id_internet_mdp').val(data.mdp);
                verrouillage_ctrl();
            },
            error: function (data) {
                toastr.error(data.responseJSON.erreur);
            }
        });
    };

</script>

<br>

"""