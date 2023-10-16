# -*- coding: utf-8 -*-
#  Copyright (c) 2019-2021 Ivan LUCAS.
#  Noethysweb, application de gestion multi-activités.
#  Distribué sous licence GNU GPL.

import logging
logger = logging.getLogger(__name__)
from core.views.mydatatableview import MyDatatable, columns
from core.views import crud
from core.models import Rattachement
from core.utils import utils_dates
from cotisations.views.saisie_lot_cotisations import Page


class Liste(Page, crud.Liste):
    model = Rattachement

    def get_queryset(self):
        return Rattachement.objects.select_related("individu", "famille").filter(self.Get_filtres("Q"))

    class datatable_class(MyDatatable):
        filtres = ["ipresent:individu", "fpresent:famille", "iscolarise:individu", "fscolarise:famille",
                   'individu__pk', "individu__nom", "individu__prenom", "famille__nom", "individu__date_naiss", "individu__rue_resid",
                   "individu__cp_resid", "individu__ville_resid"]
        check = columns.CheckBoxSelectColumn(label="")
        nom = columns.TextColumn("Nom", sources=['individu__nom'])
        prenom = columns.TextColumn("Prénom", sources=['individu__prenom'])
        famille = columns.TextColumn("Famille", sources=['famille__nom'])
        date_naiss = columns.TextColumn("Date naiss.", processor="Get_date_naiss")
        age = columns.TextColumn("Age", sources=['Get_age'], processor="Get_age")

        class Meta:
            structure_template = MyDatatable.structure_template
            columns = ["check", "idrattachement", "nom", "prenom", "age", "date_naiss", "famille"]
            ordering = ["nom", "prenom"]

        def Get_age(self, instance, *args, **kwargs):
            return instance.individu.Get_age()

        def Get_date_naiss(self, instance, *args, **kwargs):
            return utils_dates.ConvertDateToFR(instance.individu.date_naiss)
