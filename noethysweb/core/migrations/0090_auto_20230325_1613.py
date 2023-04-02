# Generated by Django 3.2.11 on 2023-03-25 16:13

import core.models
import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion
import django_cryptography.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0089_auto_20230325_1147'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collaborateur',
            fields=[
                ('idcollaborateur', models.AutoField(db_column='IDcollaborateur', primary_key=True, serialize=False, verbose_name='ID')),
                ('civilite', models.CharField(choices=[('M', 'M.'), ('MME', 'Mme')], default='M', max_length=50, verbose_name='Civilité')),
                ('nom', models.CharField(max_length=200, verbose_name='Nom')),
                ('nom_jfille', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nom de naissance')),
                ('prenom', models.CharField(blank=True, max_length=200, null=True, verbose_name='Prénom')),
                ('rue_resid', django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=200, null=True, verbose_name='Rue'))),
                ('cp_resid', django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=50, null=True, verbose_name='Code postal'))),
                ('ville_resid', django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=200, null=True, verbose_name='Ville'))),
                ('travail_tel', django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=100, null=True, verbose_name='Téléphone pro.'))),
                ('travail_mail', django_cryptography.fields.encrypt(models.EmailField(blank=True, max_length=300, null=True, verbose_name='Email pro.'))),
                ('tel_domicile', django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=100, null=True, verbose_name='Tél domicile'))),
                ('tel_mobile', django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=100, null=True, verbose_name='Tél portable'))),
                ('mail', django_cryptography.fields.encrypt(models.EmailField(blank=True, max_length=300, null=True, verbose_name='Email personnel'))),
                ('memo', models.TextField(blank=True, null=True, verbose_name='Mémo')),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Date de création')),
                ('etat', models.CharField(blank=True, max_length=50, null=True, verbose_name='Etat')),
                ('photo', models.ImageField(blank=True, null=True, upload_to=core.models.get_uuid_path, verbose_name='Photo')),
            ],
            options={
                'verbose_name': 'collaborateur',
                'verbose_name_plural': 'collaborateurs',
                'db_table': 'collaborateurs',
            },
        ),
        migrations.CreateModel(
            name='TypeQualificationCollaborateur',
            fields=[
                ('idtype_qualification', models.AutoField(db_column='IDtype_qualification', primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=300, verbose_name='Nom')),
            ],
            options={
                'verbose_name': 'type de qualification',
                'verbose_name_plural': 'types de qualifications',
                'db_table': 'types_qualifications',
            },
        ),
        migrations.AlterModelOptions(
            name='utilisateur',
            options={'permissions': [('organisateur_ajouter', 'Paramétrage | Organisateur'), ('structures_liste', 'Paramétrage | Structures'), ('types_groupes_activites_liste', "Paramétrage | Groupes d'activités"), ('activites_liste', 'Paramétrage | Activités'), ('types_cotisations_liste', "Paramétrage | Types d'adhésions"), ('unites_cotisations_liste', "Paramétrage | Unités d'adhésions"), ('questions_liste', 'Paramétrage | Questionnaires'), ('modeles_documents_liste', 'Paramétrage | Modèles de documents'), ('modeles_emails_liste', "Paramétrage | Modèles d'emails"), ('modeles_sms_liste', 'Paramétrage | Modèles de SMS'), ('modeles_rappels_liste', 'Paramétrage | Modèles de lettres de rappel'), ('modeles_pes_liste', "Paramétrage | Modèles d'exports vers le Trésor Public"), ('modeles_prestations_liste', 'Paramétrage | Modèles de prestations'), ('modeles_prelevements_liste', 'Paramétrage | Modèles de prélèvements'), ('comptes_bancaires_liste', 'Paramétrage | Comptes bancaires'), ('modes_reglements_liste', 'Paramétrage | Modes de règlements'), ('emetteurs_liste', 'Paramétrage | Emetteurs de règlements'), ('postes_analytiques_liste', 'Paramétrage | Postes analytiques'), ('comptes_comptables_liste', 'Paramétrage | Comptes comptables'), ('categories_comptables_liste', 'Paramétrage | Catégories comptables'), ('tiers_liste', 'Paramétrage | Tiers'), ('budgets_liste', 'Paramétrage | Budgets'), ('types_pieces_liste', 'Paramétrage | Types de pièces'), ('regimes_liste', 'Paramétrage | Régimes sociaux'), ('caisses_liste', 'Paramétrage | Caisses'), ('types_quotients_liste', 'Paramétrage | Types de quotients'), ('categories_travail_liste', 'Paramétrage | Catégories socio-professionnelles'), ('secteurs_liste', 'Paramétrage | Secteurs géographiques'), ('types_sieste_liste', 'Paramétrage | Types de sieste'), ('types_regimes_alimentaires_liste', 'Paramétrage | Types de régimes alimentaires'), ('categories_informations_liste', "Paramétrage | Catégories d'infos personnelles"), ('types_maladies_liste', 'Paramétrage | Types de maladies'), ('types_vaccins_liste', 'Paramétrage | Types de vaccins'), ('medecins_liste', 'Paramétrage | Médecins'), ('assureurs_liste', 'Paramétrage | Assureurs'), ('lots_factures_liste', 'Paramétrage | Lots de factures'), ('prefixes_factures_liste', 'Paramétrage | Préfixes de factures'), ('messages_factures_liste', 'Paramétrage | Messages de factures'), ('regies_liste', 'Paramétrage | Régies'), ('niveaux_scolaires_liste', 'Paramétrage | Niveaux scolaires'), ('ecoles_liste', 'Paramétrage | Ecoles'), ('classes_liste', 'Paramétrage | Classes'), ('restaurateurs_liste', 'Paramétrage | Restaurateurs'), ('menus_categories_liste', 'Paramétrage | Catégories de menus'), ('menus_legendes_liste', 'Paramétrage | Légendes de menus'), ('notes_categories_liste', 'Paramétrage | Catégories de notes'), ('taches_recurrentes_liste', 'Paramétrage | Tâches récurrentes'), ('adresses_mail_liste', "Paramétrage | Adresses d'expédition d'emails"), ('signatures_emails_liste', "Paramétrage | Signatures d'emails"), ('listes_diffusion_liste', 'Paramétrage | Listes de diffusion'), ('configurations_sms_liste', 'Paramétrage | Configurations SMS'), ('vacances_liste', 'Paramétrage | Périodes de vacances'), ('feries_fixes_liste', 'Paramétrage | Jours fériés fixes'), ('feries_variables_liste', 'Paramétrage | Jours fériés variables'), ('portail_parametres_modifier', 'Paramétrage | Paramètres généraux'), ('portail_parametres_renseignements_modifier', 'Paramétrage | Paramètres des renseignements'), ('categories_compte_internet_liste', 'Paramétrage | Catégories de compte internet'), ('types_consentements_liste', 'Paramétrage | Types de consentements'), ('unites_consentements_liste', 'Paramétrage | Unités de consentements'), ('albums_liste', 'Paramétrage | Albums photos'), ('images_articles_liste', "Paramétrage | Banque d'images des articles"), ('articles_liste', 'Paramétrage | Articles'), ('images_fond_liste', "Paramétrage | Banque d'images de fond"), ('portail_documents_liste', 'Paramétrage | Documents à télécharger'), ('categories_produits_liste', 'Paramétrage | Catégories de produits'), ('produits_liste', 'Paramétrage | Produits'), ('types_qualifications_collaborateurs_liste', 'Paramétrage | Types de qualifications'), ('statistiques', 'Outils | Statistiques générales'), ('statistiques_portail', 'Outils | Statistiques du portail'), ('contacts_liste', "Outils | Carnets d'adresses"), ('editeur_emails', "Outils | Editeur d'Emails"), ('emails_liste', 'Outils | Liste des Emails'), ('editeur_sms', 'Outils | Editeur de SMS'), ('sms_liste', 'Outils | Liste des SMS'), ('historique', 'Outils | Historique'), ('notes_liste', 'Outils | Notes'), ('taches_liste', 'Outils | Tâches'), ('update', "Outils | Mise à jour de l'application"), ('notes_versions', 'Outils | Notes de versions'), ('utilisateurs_bloques_liste', 'Outils | Utilisateurs bloqués'), ('calendrier_annuel', 'Outils | Calendrier annuel'), ('sauvegarde_creer', 'Outils | Créer une sauvegarde'), ('messagerie_portail', 'Outils | Messages non lus à traiter'), ('messages_portail_liste', 'Outils | Messages du portail'), ('demandes_portail_liste', 'Outils | Historique du portail'), ('correcteur', "Outils | Correcteur d'anomalies"), ('liste_conso_sans_presta', 'Outils | Liste des consommations sans prestations'), ('procedures', 'Outils | Procédures'), ('famille_liste', 'Individus | Liste des familles'), ('individu_liste', 'Individus | Liste des individus rattachés'), ('individus_detaches_liste', 'Individus | Liste des individus détachés'), ('individus_doublons_liste', 'Individus | Liste des individus en doublon'), ('individus_recherche_avancee', "Individus | Recherche avancée d'individus"), ('effacer_familles', 'Individus | Effacer des fiches familles'), ('inscriptions_liste', 'Individus | Liste des inscriptions'), ('liste_inscriptions_attente', 'Individus | Liste des inscriptions en attente'), ('liste_inscriptions_refus', 'Individus | Liste des inscriptions refusées'), ('inscriptions_activite_liste', 'Individus | Liste des inscriptions à une activité'), ('liste_familles_sans_inscriptions', 'Individus | Liste des familles sans inscriptions'), ('suivi_inscriptions', 'Individus | Suivi des inscriptions'), ('inscriptions_impression', 'Individus | Imprimer des inscriptions'), ('inscriptions_email', 'Individus | Envoyer des inscriptions par Email'), ('inscriptions_modifier', 'Individus | Modifier des inscriptions par lot'), ('inscriptions_scolaires_liste', 'Individus | Inscriptions scolaires'), ('scolarites_liste', 'Individus | Etapes de scolarité'), ('edition_renseignements', 'Individus | Edition des fiches de renseignements'), ('liste_anniversaires', 'Individus | Edition des anniversaires'), ('liste_regimes_caisses', 'Individus | Liste des régimes et des caisses'), ('liste_quotients', 'Individus | Liste des quotients familiaux/revenus'), ('liste_codes_comptables', 'Individus | Liste des codes comptables'), ('liste_titulaires_helios', 'Individus | Liste des titulaires Hélios'), ('mandats_liste', 'Individus | Liste des mandats SEPA'), ('contacts_urgence_liste', "Individus | Liste des contacts d'urgence et de sortie"), ('edition_contacts', 'Individus | Edition des contacts'), ('regimes_alimentaires_liste', 'Individus | Liste des régimes alimentaires'), ('maladies_liste', 'Individus | Liste des maladies'), ('informations_liste', 'Individus | Liste des informations personnelles'), ('edition_informations', 'Individus | Edition des informations et régimes'), ('liste_comptes_internet', 'Individus | Liste des comptes internet'), ('liste_pieces_manquantes', 'Individus | Liste des pièces manquantes'), ('liste_pieces_fournies', 'Individus | Liste des pièces fournies'), ('questionnaires_familles_liste', 'Individus | Liste des questionnaires familiaux'), ('questionnaires_individus_liste', 'Individus | Liste des questionnaires individuels'), ('etiquettes_individus', "Individus | Edition d'étiquettes et de badges"), ('liste_photos_manquantes', 'Individus | Liste des photos manquantes'), ('importation_photos', 'Individus | Importer des photos individuelles'), ('locations_liste', 'Locations | Liste des locations'), ('locations_impression', 'Locations | Imprimer des locations'), ('locations_email', 'Locations | Envoyer des locations par Email'), ('planning_locations', 'Locations | Planning des locations'), ('cotisations_liste', 'Adhésions | Liste des adhésions'), ('cotisations_impression', 'Adhésions | Imprimer des adhésions'), ('cotisations_email', 'Adhésions | Envoyer des adhésions par Email'), ('liste_cotisations_manquantes', 'Adhésions | Liste des adhésions manquantes'), ('saisie_lot_cotisations', "Adhésions | Saisir un lot d'adhésions"), ('liste_cotisations_disponibles', 'Adhésions | Liste des adhésions non déposées'), ('depots_cotisations_liste', "Adhésions | Dépôts d'adhésions"), ('edition_liste_conso', 'Consommations | Edition de la liste des consommations'), ('gestionnaire_conso', 'Consommations | Gestionnaire des consommations'), ('pointeuse_conso', 'Consommations | Pointeuse en temps réel'), ('suivi_consommations', 'Consommations | Suivi des consommations'), ('liste_consommations', 'Consommations | Liste des consommations'), ('liste_attente', "Consommations | Liste d'attente"), ('liste_refus', 'Consommations | Liste des places refusées'), ('liste_absences', 'Consommations | Liste des absences'), ('liste_repas', 'Consommations | Liste des repas'), ('liste_durees', 'Consommations | Liste des durées'), ('etat_global', 'Consommations | Etat global'), ('etat_nomin', 'Consommations | Etat nominatif'), ('synthese_consommations', 'Consommations | Synthèse des consommations'), ('factures_generation', 'Facturation | Génération des factures'), ('lots_pes_liste', 'Facturation | Exports vers le Trésor Public'), ('lots_prelevements_liste', 'Facturation | Prélèvements'), ('factures_impression', 'Facturation | Imprimer des factures'), ('factures_email', 'Facturation | Envoyer des factures par Email'), ('liste_factures', 'Facturation | Liste des factures'), ('rappels_generation', 'Facturation | Génération des lettres de rappel'), ('liste_rappels', 'Facturation | Liste des lettres de rappel'), ('rappels_impression', 'Facturation | Imprimer des lettres de rappel'), ('rappels_email', 'Facturation | Envoyer des lettres de rappel par Email'), ('attestations_fiscales_generation', 'Facturation | Génération des attestations fiscales'), ('liste_attestations_fiscales', 'Facturation | Liste des attestations fiscales'), ('attestations_fiscales_impression', 'Facturation | Imprimer des attestations fiscales'), ('attestations_fiscales_email', 'Facturation | Envoyer des attestations fiscales par Email'), ('liste_tarifs', 'Facturation | Liste des tarifs'), ('liste_prestations', 'Facturation | Liste des prestations'), ('liste_deductions', 'Facturation | Liste des déductions'), ('liste_soldes', 'Facturation | Liste des soldes'), ('synthese_prestations', 'Facturation | Synthèse des prestations'), ('edition_prestations', 'Facturation | Edition des prestations'), ('recalculer_prestations', 'Facturation | Recalculer des prestations'), ('synthese_impayes', 'Facturation | Synthèse des impayés'), ('liste_recus', 'Règlements | Liste des reçus de règlements'), ('liste_reglements', 'Règlements | Liste des règlements'), ('liste_detaillee_reglements', 'Règlements | Liste détaillée des règlements'), ('liste_paiements', 'Règlements | Liste des paiements en ligne'), ('detail_prestations_depot', "Règlements | Détail des prestations d'un dépôt"), ('synthese_modes_reglements', 'Règlements | Synthèse des modes de règlements'), ('liste_reglements_disponibles', 'Règlements | Liste des règlements non déposés'), ('depots_reglements_liste', 'Règlements | Dépôts de règlements'), ('corriger_ventilation', 'Règlements | Corriger la ventilation'), ('comptabilite_liste_comptes', 'Comptabilité | Liste des comptes'), ('operations_tresorerie_liste', 'Comptabilité | Liste des opérations de trésorerie'), ('operations_budgetaires_liste', 'Comptabilité | Liste des opérations budgétaires'), ('virements_liste', 'Comptabilité | Liste des virements'), ('suivi_tresorerie', 'Comptabilité | Suivi de la trésorerie'), ('suivi_budget', 'Comptabilité | Suivi du budget'), ('famille_resume', 'Fiche famille | Résumé'), ('famille_questionnaire', 'Fiche famille | Questionnaire'), ('famille_pieces', 'Fiche famille | Pièces'), ('famille_locations', 'Fiche famille | Locations'), ('famille_cotisations', 'Fiche famille | Adhésions'), ('famille_caisse', 'Fiche famille | Caisse'), ('famille_aides', 'Fiche famille | Aides'), ('famille_quotients', 'Fiche famille | Quotients familiaux'), ('famille_prestations', 'Fiche famille | Prestations'), ('famille_factures', 'Fiche famille | Factures'), ('famille_reglements', 'Fiche famille | Règlements'), ('famille_portail', 'Fiche famille | Portail'), ('famille_divers', 'Fiche famille | Paramètres'), ('famille_outils', 'Fiche famille | Outils'), ('famille_consommations', 'Fiche famille | Consommations'), ('individu_resume', 'Fiche individuelle | Résumé'), ('individu_identite', 'Fiche individuelle | Identité'), ('individu_questionnaire', 'Fiche individuelle | Questionnaire'), ('individu_liens', 'Fiche individuelle | Liens'), ('individu_coords', 'Fiche individuelle | Coordonnées'), ('individu_scolarite', 'Fiche individuelle | Scolarité'), ('individu_inscriptions', 'Fiche individuelle | Inscriptions'), ('individu_regimes_alimentaires', 'Fiche individuelle | Régimes alimentaires'), ('individu_maladies', 'Fiche individuelle | Maladies'), ('individu_medical', 'Fiche individuelle | Médical'), ('individu_assurances', 'Fiche individuelle | Assurances'), ('individu_contacts', 'Fiche individuelle | Contacts'), ('individu_consommations', 'Fiche individuelle | Consommations')]},
        ),
        migrations.CreateModel(
            name='TypePieceCollaborateur',
            fields=[
                ('idtype_piece', models.AutoField(db_column='IDtype_piece', primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200, verbose_name='Nom')),
                ('duree_validite', models.CharField(blank=True, max_length=100, null=True, verbose_name='Durée de validité')),
                ('qualifications', models.ManyToManyField(blank=True, related_name='type_piece_qualifications', to='core.TypeQualificationCollaborateur', verbose_name='Qualifications associées')),
                ('structure', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.structure', verbose_name='Structure')),
            ],
            options={
                'verbose_name': 'type de pièce',
                'verbose_name_plural': 'types de pièce',
                'db_table': 'types_pieces_collaborateur',
            },
        ),
        migrations.CreateModel(
            name='PieceCollaborateur',
            fields=[
                ('idpiece', models.AutoField(db_column='IDpiece', primary_key=True, serialize=False, verbose_name='ID')),
                ('date_debut', models.DateField(blank=True, null=True, verbose_name='Date de début')),
                ('date_fin', models.DateField(blank=True, null=True, verbose_name='Date de fin')),
                ('document', models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage, upload_to=core.models.get_uuid_path, verbose_name='Document')),
                ('titre', models.CharField(blank=True, max_length=200, null=True, verbose_name='Titre')),
                ('observations', models.TextField(blank=True, null=True, verbose_name='Observations')),
                ('collaborateur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.collaborateur', verbose_name='Collaborateur')),
                ('type_piece', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.typepiececollaborateur', verbose_name='Type de pièce')),
            ],
            options={
                'verbose_name': 'pièce',
                'verbose_name_plural': 'pièces',
                'db_table': 'pieces_collaborateur',
            },
        ),
        migrations.AddField(
            model_name='collaborateur',
            name='qualifications',
            field=models.ManyToManyField(blank=True, related_name='collaborateur_qualifications', to='core.TypeQualificationCollaborateur', verbose_name='Qualifications'),
        ),
    ]
