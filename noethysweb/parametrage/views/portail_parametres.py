# -*- coding: utf-8 -*-
#  Copyright (c) 2019-2021 Ivan LUCAS.
#  Noethysweb, application de gestion multi-activités.
#  Distribué sous licence GNU GPL.

from django.urls import reverse_lazy
from parametrage.forms.portail_parametres import Formulaire
from core.views.base import CustomView
from core.models import PortailParametre
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect


class Modifier(CustomView, TemplateView):
    template_name = "core/crud/edit.html"
    compatible_demo = False

    def get_context_data(self, **kwargs):
        context = super(Modifier, self).get_context_data(**kwargs)
        context['page_titre'] = "Paramètres du portail"
        context['box_titre'] = "Paramètres"
        context['box_introduction'] = "Ajustez les paramètres du portail et cliquez sur le bouton Enregistrer."
        # context['afficher_menu_brothers'] = True
        context['form'] = context.get("form", Formulaire)
        return context

    def post(self, request, **kwargs):
        form = Formulaire(request.POST, request=self.request)
        if not form.is_valid():
            return self.render_to_response(self.get_context_data(form=form))

        # Enregistrement
        for code, valeur in form.cleaned_data.items():
            objet, created = PortailParametre.objects.update_or_create(code=code, defaults={'valeur': str(valeur)})

        return HttpResponseRedirect(reverse_lazy("parametrage_toc"))