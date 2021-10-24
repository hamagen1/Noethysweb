# Generated by Django 3.2.8 on 2021-10-24 15:47

import core.models
import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_auto_20211024_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assurance',
            name='document',
            field=models.FileField(blank=True, help_text='Vous pouvez ajouter un document (PDF ou image).', null=True, storage=django.core.files.storage.FileSystemStorage, upload_to=core.models.get_uuid_path, verbose_name='Document'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='fichier',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage, upload_to=core.models.get_uuid_path, verbose_name='Fichier'),
        ),
        migrations.AlterField(
            model_name='piece',
            name='document',
            field=models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage, upload_to=core.models.get_uuid_path, verbose_name='Document'),
        ),
        migrations.AlterField(
            model_name='problemesante',
            name='document',
            field=models.FileField(blank=True, help_text='Vous pouvez ajouter un document.', null=True, storage=django.core.files.storage.FileSystemStorage, upload_to=core.models.get_uuid_path, verbose_name='Document'),
        ),
        migrations.AlterField(
            model_name='quotient',
            name='document',
            field=models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage, upload_to=core.models.get_uuid_path, verbose_name='Document'),
        ),
    ]
