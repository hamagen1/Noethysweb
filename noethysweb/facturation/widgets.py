# -*- coding: utf-8 -*-

#  Copyright (c) 2019-2021 Ivan LUCAS.
#  Noethysweb, application de gestion multi-activités.
#  Distribué sous licence GNU GPL.

from django.forms.utils import flatatt
from django.forms.widgets import Widget, Textarea
from django.template import loader
from django.utils.safestring import mark_safe


class ProchainNumeroWidget(Widget):
    template_name = 'facturation/widgets/prochain_numero.html'

    def get_context(self, name, value, attrs=None):
        context = dict(self.attrs.items())
        if attrs is not None:
            context.update(attrs)
        context['name'] = name
        if value is not None:
            context['value'] = value
        return context

    def render(self, name, value, attrs=None, renderer=None):
        context = self.get_context(name, value, attrs)
        return mark_safe(loader.render_to_string(self.template_name, context))

    def value_from_datadict(self, data, files, name):
        if data.get("checkbox_prochain_numero") == "true":
            return "auto"
        else:
            return data.get("prochain_numero")
