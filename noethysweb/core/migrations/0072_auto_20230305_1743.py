# Generated by Django 3.2.11 on 2023-03-05 17:43

import core.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0071_auto_20230304_0843'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategorieProduit',
            fields=[
                ('idcategorie', models.AutoField(db_column='IDcategorie', primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200, verbose_name='Nom')),
                ('observations', models.TextField(blank=True, null=True, verbose_name='Observations')),
                ('image', models.ImageField(blank=True, null=True, upload_to=core.models.get_uuid_path, verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Catégorie de produits',
                'verbose_name_plural': 'Catégories de produits',
                'db_table': 'produits_categories',
            },
        ),
        migrations.AlterModelOptions(
            name='utilisateur',
            options={'permissions': [('organisateur_ajouter', 'Paramétrage | Organisateur'), ('structures_liste', 'Paramétrage | Structures'), ('types_groupes_activites_liste', "Paramétrage | Groupes d'activités"), ('activites_liste', 'Paramétrage | Activités'), ('types_cotisations_liste', "Paramétrage | Types d'adhésions"), ('unites_cotisations_liste', "Paramétrage | Unités d'adhésions"), ('questions_liste', 'Paramétrage | Questionnaires'), ('modeles_documents_liste', 'Paramétrage | Modèles de documents'), ('modeles_emails_liste', "Paramétrage | Modèles d'emails"), ('modeles_sms_liste', 'Paramétrage | Modèles de SMS'), ('modeles_rappels_liste', 'Paramétrage | Modèles de lettres de rappel'), ('modeles_pes_liste', "Paramétrage | Modèles d'exports vers le Trésor Public"), ('modeles_prestations_liste', 'Paramétrage | Modèles de prestations'), ('modeles_prelevements_liste', 'Paramétrage | Modèles de prélèvements'), ('comptes_bancaires_liste', 'Paramétrage | Comptes bancaires'), ('modes_reglements_liste', 'Paramétrage | Modes de règlements'), ('emetteurs_liste', 'Paramétrage | Emetteurs de règlements'), ('types_pieces_liste', 'Paramétrage | Types de pièces'), ('regimes_liste', 'Paramétrage | Régimes sociaux'), ('caisses_liste', 'Paramétrage | Caisses'), ('types_quotients_liste', 'Paramétrage | Types de quotients'), ('categories_travail_liste', 'Paramétrage | Catégories socio-professionnelles'), ('secteurs_liste', 'Paramétrage | Secteurs géographiques'), ('types_sieste_liste', 'Paramétrage | Types de sieste'), ('types_regimes_alimentaires_liste', 'Paramétrage | Types de régimes alimentaires'), ('categories_informations_liste', "Paramétrage | Catégories d'infos personnelles"), ('types_maladies_liste', 'Paramétrage | Types de maladies'), ('types_vaccins_liste', 'Paramétrage | Types de vaccins'), ('medecins_liste', 'Paramétrage | Médecins'), ('assureurs_liste', 'Paramétrage | Assureurs'), ('lots_factures_liste', 'Paramétrage | Lots de factures'), ('prefixes_factures_liste', 'Paramétrage | Préfixes de factures'), ('messages_factures_liste', 'Paramétrage | Messages de factures'), ('regies_liste', 'Paramétrage | Régies'), ('niveaux_scolaires_liste', 'Paramétrage | Niveaux scolaires'), ('ecoles_liste', 'Paramétrage | Ecoles'), ('classes_liste', 'Paramétrage | Classes'), ('restaurateurs_liste', 'Paramétrage | Restaurateurs'), ('menus_categories_liste', 'Paramétrage | Catégories de menus'), ('menus_legendes_liste', 'Paramétrage | Légendes de menus'), ('notes_categories_liste', 'Paramétrage | Catégories de notes'), ('taches_recurrentes_liste', 'Paramétrage | Tâches récurrentes'), ('adresses_mail_liste', "Paramétrage | Adresses d'expédition d'emails"), ('signatures_emails_liste', "Paramétrage | Signatures d'emails"), ('listes_diffusion_liste', 'Paramétrage | Listes de diffusion'), ('configurations_sms_liste', 'Paramétrage | Configurations SMS'), ('vacances_liste', 'Paramétrage | Périodes de vacances'), ('feries_fixes_liste', 'Paramétrage | Jours fériés fixes'), ('feries_variables_liste', 'Paramétrage | Jours fériés variables'), ('portail_parametres_modifier', 'Paramétrage | Paramètres généraux'), ('portail_parametres_renseignements_modifier', 'Paramétrage | Paramètres des renseignements'), ('categories_compte_internet_liste', 'Paramétrage | Catégories de compte internet'), ('types_consentements_liste', 'Paramétrage | Types de consentements'), ('unites_consentements_liste', 'Paramétrage | Unités de consentements'), ('albums_liste', 'Paramétrage | Albums photos'), ('images_articles_liste', "Paramétrage | Banque d'images des articles"), ('articles_liste', 'Paramétrage | Articles'), ('images_fond_liste', "Paramétrage | Banque d'images de fond"), ('portail_documents_liste', 'Paramétrage | Documents à télécharger'), ('categories_produits_liste', 'Paramétrage | Catégories de produits'), ('statistiques', 'Outils | Statistiques générales'), ('statistiques_portail', 'Outils | Statistiques du portail'), ('contacts_liste', "Outils | Carnets d'adresses"), ('editeur_emails', "Outils | Editeur d'Emails"), ('emails_liste', 'Outils | Liste des Emails'), ('editeur_sms', 'Outils | Editeur de SMS'), ('sms_liste', 'Outils | Liste des SMS'), ('historique', 'Outils | Historique'), ('notes_liste', 'Outils | Notes'), ('taches_liste', 'Outils | Tâches'), ('update', "Outils | Mise à jour de l'application"), ('notes_versions', 'Outils | Notes de versions'), ('utilisateurs_bloques_liste', 'Outils | Utilisateurs bloqués'), ('calendrier_annuel', 'Outils | Calendrier annuel'), ('sauvegarde_creer', 'Outils | Créer une sauvegarde'), ('messagerie_portail', 'Outils | Messages non lus à traiter'), ('messages_portail_liste', 'Outils | Messages du portail'), ('demandes_portail_liste', 'Outils | Historique du portail'), ('correcteur', "Outils | Correcteur d'anomalies"), ('liste_conso_sans_presta', 'Outils | Liste des consommations sans prestations'), ('procedures', 'Outils | Procédures'), ('famille_liste', 'Individus | Liste des familles'), ('individu_liste', 'Individus | Liste des individus rattachés'), ('individus_detaches_liste', 'Individus | Liste des individus détachés'), ('individus_doublons_liste', 'Individus | Liste des individus en doublon'), ('individus_recherche_avancee', "Individus | Recherche avancée d'individus"), ('effacer_familles', 'Individus | Effacer des fiches familles'), ('inscriptions_liste', 'Individus | Liste des inscriptions'), ('liste_inscriptions_attente', 'Individus | Liste des inscriptions en attente'), ('liste_inscriptions_refus', 'Individus | Liste des inscriptions refusées'), ('inscriptions_activite_liste', 'Individus | Liste des inscriptions à une activité'), ('liste_familles_sans_inscriptions', 'Individus | Liste des familles sans inscriptions'), ('suivi_inscriptions', 'Individus | Suivi des inscriptions'), ('inscriptions_impression', 'Individus | Imprimer des inscriptions'), ('inscriptions_email', 'Individus | Envoyer des inscriptions par Email'), ('inscriptions_modifier', 'Individus | Modifier des inscriptions par lot'), ('inscriptions_scolaires_liste', 'Individus | Inscriptions scolaires'), ('scolarites_liste', 'Individus | Etapes de scolarité'), ('edition_renseignements', 'Individus | Edition des fiches de renseignements'), ('liste_anniversaires', 'Individus | Edition des anniversaires'), ('liste_regimes_caisses', 'Individus | Liste des régimes et des caisses'), ('liste_quotients', 'Individus | Liste des quotients familiaux/revenus'), ('liste_codes_comptables', 'Individus | Liste des codes comptables'), ('liste_titulaires_helios', 'Individus | Liste des titulaires Hélios'), ('mandats_liste', 'Individus | Liste des mandats SEPA'), ('contacts_urgence_liste', "Individus | Liste des contacts d'urgence et de sortie"), ('edition_contacts', 'Individus | Edition des contacts'), ('regimes_alimentaires_liste', 'Individus | Liste des régimes alimentaires'), ('maladies_liste', 'Individus | Liste des maladies'), ('informations_liste', 'Individus | Liste des informations personnelles'), ('edition_informations', 'Individus | Edition des informations et régimes'), ('liste_comptes_internet', 'Individus | Liste des comptes internet'), ('liste_pieces_manquantes', 'Individus | Liste des pièces manquantes'), ('liste_pieces_fournies', 'Individus | Liste des pièces fournies'), ('questionnaires_familles_liste', 'Individus | Liste des questionnaires familiaux'), ('questionnaires_individus_liste', 'Individus | Liste des questionnaires individuels'), ('etiquettes_individus', "Individus | Edition d'étiquettes et de badges"), ('liste_photos_manquantes', 'Individus | Liste des photos manquantes'), ('importation_photos', 'Individus | Importer des photos individuelles'), ('cotisations_liste', 'Adhésions | Liste des adhésions'), ('cotisations_impression', 'Adhésions | Imprimer des adhésions'), ('cotisations_email', 'Adhésions | Envoyer des adhésions par Email'), ('liste_cotisations_manquantes', 'Adhésions | Liste des adhésions manquantes'), ('saisie_lot_cotisations', "Adhésions | Saisir un lot d'adhésions"), ('liste_cotisations_disponibles', 'Adhésions | Liste des adhésions non déposées'), ('depots_cotisations_liste', "Adhésions | Dépôts d'adhésions"), ('edition_liste_conso', 'Consommations | Edition de la liste des consommations'), ('gestionnaire_conso', 'Consommations | Gestionnaire des consommations'), ('pointeuse_conso', 'Consommations | Pointeuse en temps réel'), ('suivi_consommations', 'Consommations | Suivi des consommations'), ('liste_consommations', 'Consommations | Liste des consommations'), ('liste_attente', "Consommations | Liste d'attente"), ('liste_refus', 'Consommations | Liste des places refusées'), ('liste_absences', 'Consommations | Liste des absences'), ('liste_repas', 'Consommations | Liste des repas'), ('liste_durees', 'Consommations | Liste des durées'), ('etat_global', 'Consommations | Etat global'), ('etat_nomin', 'Consommations | Etat nominatif'), ('synthese_consommations', 'Consommations | Synthèse des consommations'), ('factures_generation', 'Facturation | Génération des factures'), ('lots_pes_liste', 'Facturation | Exports vers le Trésor Public'), ('lots_prelevements_liste', 'Facturation | Prélèvements'), ('factures_impression', 'Facturation | Imprimer des factures'), ('factures_email', 'Facturation | Envoyer des factures par Email'), ('liste_factures', 'Facturation | Liste des factures'), ('rappels_generation', 'Facturation | Génération des lettres de rappel'), ('liste_rappels', 'Facturation | Liste des lettres de rappel'), ('rappels_impression', 'Facturation | Imprimer des lettres de rappel'), ('rappels_email', 'Facturation | Envoyer des lettres de rappel par Email'), ('attestations_fiscales_generation', 'Facturation | Génération des attestations fiscales'), ('liste_attestations_fiscales', 'Facturation | Liste des attestations fiscales'), ('attestations_fiscales_impression', 'Facturation | Imprimer des attestations fiscales'), ('attestations_fiscales_email', 'Facturation | Envoyer des attestations fiscales par Email'), ('liste_tarifs', 'Facturation | Liste des tarifs'), ('liste_prestations', 'Facturation | Liste des prestations'), ('liste_deductions', 'Facturation | Liste des déductions'), ('liste_soldes', 'Facturation | Liste des soldes'), ('synthese_prestations', 'Facturation | Synthèse des prestations'), ('edition_prestations', 'Facturation | Edition des prestations'), ('recalculer_prestations', 'Facturation | Recalculer des prestations'), ('synthese_impayes', 'Facturation | Synthèse des impayés'), ('liste_recus', 'Règlements | Liste des reçus de règlements'), ('liste_reglements', 'Règlements | Liste des règlements'), ('liste_detaillee_reglements', 'Règlements | Liste détaillée des règlements'), ('liste_paiements', 'Règlements | Liste des paiements en ligne'), ('detail_prestations_depot', "Règlements | Détail des prestations d'un dépôt"), ('synthese_modes_reglements', 'Règlements | Synthèse des modes de règlements'), ('liste_reglements_disponibles', 'Règlements | Liste des règlements non déposés'), ('depots_reglements_liste', 'Règlements | Dépôts de règlements'), ('corriger_ventilation', 'Règlements | Corriger la ventilation'), ('famille_resume', 'Fiche famille | Résumé'), ('famille_questionnaire', 'Fiche famille | Questionnaire'), ('famille_pieces', 'Fiche famille | Pièces'), ('famille_cotisations', 'Fiche famille | Adhésions'), ('famille_caisse', 'Fiche famille | Caisse'), ('famille_aides', 'Fiche famille | Aides'), ('famille_quotients', 'Fiche famille | Quotients familiaux'), ('famille_prestations', 'Fiche famille | Prestations'), ('famille_factures', 'Fiche famille | Factures'), ('famille_reglements', 'Fiche famille | Règlements'), ('famille_portail', 'Fiche famille | Portail'), ('famille_divers', 'Fiche famille | Paramètres'), ('famille_outils', 'Fiche famille | Outils'), ('famille_consommations', 'Fiche famille | Consommations'), ('individu_resume', 'Fiche individuelle | Résumé'), ('individu_identite', 'Fiche individuelle | Identité'), ('individu_questionnaire', 'Fiche individuelle | Questionnaire'), ('individu_liens', 'Fiche individuelle | Liens'), ('individu_coords', 'Fiche individuelle | Coordonnées'), ('individu_scolarite', 'Fiche individuelle | Scolarité'), ('individu_inscriptions', 'Fiche individuelle | Inscriptions'), ('individu_regimes_alimentaires', 'Fiche individuelle | Régimes alimentaires'), ('individu_maladies', 'Fiche individuelle | Maladies'), ('individu_medical', 'Fiche individuelle | Médical'), ('individu_assurances', 'Fiche individuelle | Assurances'), ('individu_contacts', 'Fiche individuelle | Contacts'), ('individu_consommations', 'Fiche individuelle | Consommations')]},
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('idproduit', models.AutoField(db_column='IDproduit', primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200, verbose_name='Nom')),
                ('observations', models.TextField(blank=True, null=True, verbose_name='Observations')),
                ('image', models.ImageField(blank=True, null=True, upload_to=core.models.get_uuid_path, verbose_name='Image')),
                ('quantite', models.IntegerField(default=1, verbose_name='Quantité')),
                ('montant', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True, verbose_name='Montant')),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.categorieproduit', verbose_name='Catégorie')),
            ],
            options={
                'verbose_name': 'produit',
                'verbose_name_plural': 'produits',
                'db_table': 'produits',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('idlocation', models.AutoField(db_column='IDlocation', primary_key=True, serialize=False, verbose_name='ID')),
                ('observations', models.TextField(blank=True, null=True, verbose_name='Observations')),
                ('date_saisie', models.DateField(auto_now_add=True, verbose_name='Date de saisie')),
                ('date_debut', models.DateTimeField(verbose_name='Début')),
                ('date_fin', models.DateTimeField(blank=True, null=True, verbose_name='Fin')),
                ('quantite', models.IntegerField(default=1, verbose_name='Quantité')),
                ('famille', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.famille', verbose_name='Famille')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.produit', verbose_name='Produit')),
            ],
            options={
                'verbose_name': 'location',
                'verbose_name_plural': 'locations',
                'db_table': 'locations',
            },
        ),
    ]
