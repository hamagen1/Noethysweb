# Generated by Django 3.2.11 on 2023-04-28 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0111_unitecotisation_prefacturation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modeleemail',
            name='categorie',
            field=models.CharField(choices=[('saisie_libre', 'Saisie libre'), ('releve_prestations', 'Relevé des prestations'), ('reglement', 'Règlement'), ('recu_reglement', 'Reçu de règlement'), ('recu_don_oeuvres', 'Reçu de don aux oeuvres'), ('facture', 'Facture'), ('rappel', 'Rappel'), ('attestation_presence', 'Attestation de présence'), ('attestation_fiscale', 'Attestation fiscale'), ('reservations', 'Liste des réservations'), ('cotisation', 'Cotisation'), ('mandat_sepa', 'Mandat SEPA'), ('rappel_pieces_manquantes', 'Rappel pièces manquantes'), ('portail', 'Rappel des données du compte internet'), ('portail_demande_inscription', "Portail - Demande d'une inscription"), ('portail_demande_reservation', "Portail - Demande d'une réservation"), ('portail_demande_renseignement', "Portail - Demande de modification d'un renseignement"), ('portail_demande_facture', "Portail - Demande d'une facture"), ('portail_demande_recu_reglement', "Portail - Demande d'un reçu de règlement"), ('portail_demande_location', "Portail - Demande d'une location"), ('portail_places_disponibles', 'Portail - Attribution de places disponibles'), ('portail_confirmation_reservations', 'Portail - Confirmation des réservations'), ('portail_notification_message', "Portail - Notification d'un message"), ('location', 'Location'), ('location_demande', 'Demande de location'), ('commande_repas', 'Commande de repas'), ('inscription', 'Inscription'), ('devis', 'Devis')], max_length=200, verbose_name='Catégorie'),
        ),
    ]
