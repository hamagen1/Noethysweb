# Generated by Django 3.2.21 on 2023-10-12 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0131_attestation_exclusions_prestations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarifligne',
            name='montant_unique',
            field=models.DecimalField(blank=True, decimal_places=3, default=0.0, max_digits=10, null=True, verbose_name='Montant unique'),
        ),
    ]
