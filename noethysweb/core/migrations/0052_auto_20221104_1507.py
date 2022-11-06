# Generated by Django 3.2.11 on 2022-11-04 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0051_alter_utilisateur_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portailperiode',
            name='prefacturation',
            field=models.BooleanField(default=False, help_text="Cochez cette case pour que la famille puisse payer les prestations de cette période sur le portail même si aucune facture n'a été générée.", verbose_name='Activer la préfacturation pour cette période'),
        ),
        migrations.CreateModel(
            name='Paiement',
            fields=[
                ('idpaiement', models.AutoField(db_column='IDpaiement', primary_key=True, serialize=False, verbose_name='ID')),
                ('idtransaction', models.CharField(blank=True, max_length=50, null=True, verbose_name='ID transaction')),
                ('refdet', models.CharField(blank=True, max_length=50, null=True, verbose_name='refdet')),
                ('montant', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Montant')),
                ('objet', models.CharField(blank=True, max_length=50, null=True, verbose_name='objet')),
                ('saisie', models.CharField(blank=True, max_length=50, null=True, verbose_name='saisie')),
                ('resultrans', models.CharField(blank=True, max_length=50, null=True, verbose_name='resultrans')),
                ('numauto', models.CharField(blank=True, max_length=50, null=True, verbose_name='numauto')),
                ('dattrans', models.CharField(blank=True, max_length=50, null=True, verbose_name='dattrans')),
                ('heurtrans', models.CharField(blank=True, max_length=50, null=True, verbose_name='heurtrans')),
                ('systeme_paiement', models.CharField(blank=True, max_length=50, null=True, verbose_name='systeme_paiement')),
                ('resultat', models.CharField(blank=True, max_length=50, null=True, verbose_name='resultat')),
                ('message', models.CharField(blank=True, max_length=450, null=True, verbose_name='message')),
                ('ventilation', models.TextField(blank=True, null=True, verbose_name='ventilation')),
                ('horodatage', models.DateTimeField(auto_now_add=True, verbose_name='horodatage')),
                ('famille', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.famille', verbose_name='Famille')),
                ('reglement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.reglement', verbose_name='Règlement')),
            ],
            options={
                'verbose_name': 'Paiement en ligne',
                'verbose_name_plural': 'Paiements en ligne',
                'db_table': 'paiements',
            },
        ),
    ]
