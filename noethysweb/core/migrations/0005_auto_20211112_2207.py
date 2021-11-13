# Generated by Django 3.2.9 on 2021-11-12 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_tarif_facturation_unite'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pespiece',
            options={'verbose_name': "pièce d'export", 'verbose_name_plural': "pièces d'export"},
        ),
        migrations.AddField(
            model_name='activite',
            name='assurance_obligatoire',
            field=models.BooleanField(default=False, verbose_name='Assurance obligatoire'),
        ),
        migrations.AlterField(
            model_name='prestation',
            name='facture',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.facture', verbose_name='Facture'),
        ),
    ]
