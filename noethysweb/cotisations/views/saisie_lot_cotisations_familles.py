# -*- coding: utf-8 -*-
#  Copyright (c) 2019-2021 Ivan LUCAS.
#  Noethysweb, application de gestion multi-activités.
#  Distribué sous licence GNU GPL.

import logging
logger = logging.getLogger(__name__)
from core.views.mydatatableview import MyDatatable, columns
from core.views import crud
from core.models import Famille
from cotisations.views.saisie_lot_cotisations import Page


class Liste(Page, crud.Liste):
    model = Famille

    def get_queryset(self):
        return Famille.objects.filter(self.Get_filtres("Q"))

    class datatable_class(MyDatatable):
        filtres = ["fpresent:pk", "fscolarise:pk", "idfamille", "nom", "rue_resid", "cp_resid", "ville_resid", "mail", "caisse__nom"]
        check = columns.CheckBoxSelectColumn(label="")
        mail = columns.TextColumn("Email", processor='Get_mail')
        rue_resid = columns.TextColumn("Rue", processor='Get_rue_resid')
        cp_resid = columns.TextColumn("CP", processor='Get_cp_resid')
        ville_resid = columns.TextColumn("Ville",  sources=None, processor='Get_ville_resid')

        class Meta:
            structure_template = MyDatatable.structure_template
            columns = ["check", "idfamille", "nom", "mail", "rue_resid", "cp_resid", "ville_resid"]
            ordering = ["nom"]

        def Get_mail(self, instance, *args, **kwargs):
            return instance.mail

        def Get_rue_resid(self, instance, *args, **kwargs):
            return instance.rue_resid

        def Get_cp_resid(self, instance, *args, **kwargs):
            return instance.cp_resid

        def Get_ville_resid(self, instance, *args, **kwargs):
            return instance.ville_resid
