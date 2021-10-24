# Generated by Django 3.2.8 on 2021-10-24 14:34

import core.models
from django.db import migrations, models
import storages.backends.dropbox


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_alter_individu_annee_deces'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piece',
            name='document',
            field=models.FileField(blank=True, null=True, storage=storages.backends.dropbox.DropBoxStorage(), upload_to=core.models.get_uuid_path, verbose_name='Document'),
        ),
        migrations.AlterField(
            model_name='portailchamp',
            name='contact',
            field=models.CharField(choices=[('MASQUER', 'Masqué'), ('AFFICHER', 'Affiché'), ('MODIFIABLE', 'Modifiable')], default='MODIFIABLE', max_length=100, verbose_name='Contact'),
        ),
        migrations.AlterField(
            model_name='portailchamp',
            name='enfant',
            field=models.CharField(choices=[('MASQUER', 'Masqué'), ('AFFICHER', 'Affiché'), ('MODIFIABLE', 'Modifiable')], default='MODIFIABLE', max_length=100, verbose_name='Enfant'),
        ),
        migrations.AlterField(
            model_name='portailchamp',
            name='famille',
            field=models.CharField(choices=[('MASQUER', 'Masqué'), ('AFFICHER', 'Affiché'), ('MODIFIABLE', 'Modifiable')], default='MODIFIABLE', max_length=100, verbose_name='Famille'),
        ),
        migrations.AlterField(
            model_name='portailchamp',
            name='representant',
            field=models.CharField(choices=[('MASQUER', 'Masqué'), ('AFFICHER', 'Affiché'), ('MODIFIABLE', 'Modifiable')], default='MODIFIABLE', max_length=100, verbose_name='Représentant'),
        ),
    ]