# Generated by Django 3.2.11 on 2022-10-31 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0048_adressemail_actif'),
    ]

    operations = [
        migrations.AddField(
            model_name='famille',
            name='tiers_solidaire',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tiers_solidaire', to='core.individu', verbose_name='Tiers solidaire'),
        ),
        migrations.AddField(
            model_name='pespiece',
            name='tiers_solidaire',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='piece_tiers_solidaire', to='core.individu', verbose_name='Tiers solidaire'),
        ),
        migrations.AlterField(
            model_name='pespiece',
            name='titulaire_helios',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='piece_titulaire_helios', to='core.individu', verbose_name='Titulaire Hélios'),
        ),
        migrations.AlterField(
            model_name='uniteremplissage',
            name='abrege',
            field=models.CharField(help_text='Le nom abrégé est généralement constitué de quelques caractères en majuscules. Exemples : J, M, SEANCE, ATELIER...', max_length=200, verbose_name='Abrégé'),
        ),
        migrations.AlterField(
            model_name='uniteremplissage',
            name='nom',
            field=models.CharField(help_text="Renseigner le nom complet de l'unité. Exemples : Journée, Matinée, Séance, Atelier...", max_length=200, verbose_name='Nom'),
        ),
        migrations.AlterField(
            model_name='uniteremplissage',
            name='seuil_alerte',
            field=models.IntegerField(default=5, help_text='Nombre de places restantes à partir duquel il faut colorer le fond de la case en jaune. Valeur conseillée : 5.', verbose_name="Seuil d'alerte"),
        ),
    ]
