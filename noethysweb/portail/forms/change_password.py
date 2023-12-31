# -*- coding: utf-8 -*-
#  Copyright (c) 2019-2021 Ivan LUCAS.
#  Noethysweb, application de gestion multi-activités.
#  Distribué sous licence GNU GPL.

from django import forms
from django.contrib.auth.forms import SetPasswordForm
from django.utils.translation import gettext as _
from portail.utils import utils_secquest


class MyPasswordChangeForm(SetPasswordForm):
    check_conditions = forms.BooleanField(label="", required=True, initial=False)
    field_order = ['new_password1', 'new_password2', 'check_conditions']

    def __init__(self, *args, **kwargs):
        super(MyPasswordChangeForm, self).__init__(*args, **kwargs)
        self.fields['new_password1'].widget.attrs['class'] = "form-control"
        self.fields['new_password1'].widget.attrs['title'] = _("Saisissez un nouveau mot de passe")
        self.fields['new_password1'].widget.attrs['placeholder'] = _("Saisissez un nouveau mot de passe")
        self.fields['new_password2'].widget.attrs['class'] = "form-control"
        self.fields['new_password2'].widget.attrs['title'] = _("Saisissez le nouveau mot de passe une nouvelle fois")
        self.fields['new_password2'].widget.attrs['placeholder'] = _("Saisissez le nouveau mot de passe une nouvelle fois")

        # Question
        if kwargs["user"].famille.internet_secquest:
            self.fields["secquest"] = utils_secquest.Generation_field_secquest(famille=kwargs["user"].famille)
