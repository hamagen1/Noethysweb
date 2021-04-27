# -*- coding: utf-8 -*-

#  Copyright (c) 2019-2021 Ivan LUCAS.
#  Noethysweb, application de gestion multi-activités.
#  Distribué sous licence GNU GPL.

from django.urls import reverse_lazy, reverse
from core.views.mydatatableview import MyDatatable, columns, helpers, Deplacer_lignes
from core.views import crud
from core.utils import utils_preferences
from parametrage.views.activites import Onglet
from core.models import Evenement, Activite, Ouverture, Tarif
from parametrage.forms.activites_evenements import Formulaire
from django.db.models import Q
from django.contrib import messages


class Page(Onglet):
    model = Evenement
    url_liste = "activites_evenements_liste"
    url_ajouter = "activites_evenements_ajouter"
    url_modifier = "activites_evenements_modifier"
    url_supprimer = "activites_evenements_supprimer"
    description_liste = "Vous pouvez saisir ici des événements pour l'activité."
    description_saisie = "Saisissez toutes les informations concernant l'événement à saisir et cliquez sur le bouton Enregistrer."
    objet_singulier = "un événement"
    objet_pluriel = "des événements"

    def get_context_data(self, **kwargs):
        """ Context data spécial pour onglet """
        context = super(Page, self).get_context_data(**kwargs)
        context['box_titre'] = "Evénements"
        context['onglet_actif'] = "evenements"
        context['boutons_liste'] = [
            {"label": "Ajouter", "classe": "btn btn-success", "href": reverse_lazy(self.url_ajouter, kwargs={'idactivite': self.Get_idactivite()}), "icone": "fa fa-plus"},
        ]
        return context

    def get_form_kwargs(self, **kwargs):
        """ Envoie l'idactivite au formulaire """
        form_kwargs = super(Page, self).get_form_kwargs(**kwargs)
        form_kwargs["idactivite"] = self.Get_idactivite()
        return form_kwargs

    def get_success_url(self):
        """ Renvoie vers la liste après le formulaire """
        url = self.url_liste
        if "SaveAndNew" in self.request.POST:
            url = self.url_ajouter
        return reverse_lazy(url, kwargs={'idactivite': self.Get_idactivite()})


class Liste(Page, crud.Liste):
    model = Evenement
    template_name = "parametrage/activite_liste.html"

    def get_queryset(self):
        return Evenement.objects.filter(Q(activite=self.Get_idactivite()) & self.Get_filtres("Q"))

    def get_context_data(self, **kwargs):
        context = super(Liste, self).get_context_data(**kwargs)
        return context

    class datatable_class(MyDatatable):
        filtres = ['idevenement', 'date', 'groupe__nom', 'nom', 'unite__nom']

        actions = columns.TextColumn("Actions", sources=None, processor='Get_actions_speciales')
        tarification = columns.TextColumn("Tarification", sources=None, processor='Get_tarification')
        groupe = columns.TextColumn("Groupe", sources=["groupe__nom"])

        class Meta:
            structure_template = MyDatatable.structure_template
            columns = ['idevenement', 'date', 'nom', 'groupe', 'tarification']
            #hidden_columns = ["idevenement"]
            ordering = ['date']
            processors = {
                'date': helpers.format_date('%d/%m/%Y'),
            }

        def Get_tarification(self, instance, *args, **kwargs):
            # Importation des tarifs avancés
            if not hasattr(self, "dict_tarifs"):
                self.dict_tarifs = {}
                for tarif in Tarif.objects.filter(evenement__isnull=False):
                    if tarif.evenement not in self.dict_tarifs:
                        self.dict_tarifs[tarif.evenement] = []
                    self.dict_tarifs[tarif.evenement].append(tarif)

            # Affichage du texte de la colonne tarification
            if instance.montant:
                return "%.2f %s" % (instance.montant, utils_preferences.Get_symbole_monnaie())
            if instance in self.dict_tarifs:
                pluriel = "s" if len(self.dict_tarifs[instance]) > 1 else ""
                texte = "%d tarif%s avancé%s" % (len(self.dict_tarifs[instance]), pluriel, pluriel)
            else:
                texte = "Gratuit"
            url_liste = reverse("activites_evenements_tarifs_liste", args=[instance.activite_id, instance.pk])
            return texte + """&nbsp; <a type='button' class='btn btn-default btn-sm' href='%s' title='Ajouter, modifier ou supprimer des tarifs avancés'><i class="fa fa-gear"></i></a>""" % url_liste

        def Get_actions_speciales(self, instance, *args, **kwargs):
            """ Inclut l'idactivite dans les boutons d'actions """
            html = [
                self.Create_bouton_modifier(url=reverse(kwargs["view"].url_modifier, args=[instance.activite.idactivite, instance.pk])),
                self.Create_bouton_supprimer(url=reverse(kwargs["view"].url_supprimer, args=[instance.activite.idactivite, instance.pk])),
            ]
            return self.Create_boutons_actions(html)



class Ajouter(Page, crud.Ajouter):
    form_class = Formulaire
    template_name = "parametrage/activite_edit.html"

    def form_valid(self, form):
        """ Après l'ajout d'un événement, on ouvre le calendrier si besoin """
        evenement = form.instance
        if Ouverture.objects.filter(date=evenement.date, groupe=evenement.groupe, unite=evenement.unite).count() == 0:
            Ouverture.objects.create(date=evenement.date, activite=evenement.activite, groupe=evenement.groupe, unite=evenement.unite)
            messages.add_message(self.request, messages.INFO, "Une ouverture a été créée automatiquement dans le calendrier")
        return super(Ajouter, self).form_valid(form)


class Modifier(Page, crud.Modifier):
    form_class = Formulaire
    template_name = "parametrage/activite_edit.html"

    def form_valid(self, form):
        """ Après la modification d'un événement, on vérifie que la date est toujours exacte dans les tarifs avancés associés """
        evenement = form.instance
        for tarif in Tarif.objects.filter(evenement=evenement):
            if tarif.date_debut != evenement.date or tarif.date_fin != evenement.date:
                tarif.date_debut = evenement.date
                tarif.date_fin = evenement.date
                tarif.save()
        return super(Modifier, self).form_valid(form)


class Supprimer(Page, crud.Supprimer):
    template_name = "parametrage/activite_delete.html"

