# Generated by Django 4.0a1 on 2021-10-04 10:41

from django.db import migrations, models
import django_cryptography.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_alter_adressemail_adresse_alter_adressemail_hote_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaccin',
            name='date',
            field=django_cryptography.fields.encrypt(models.DateField(verbose_name='Date de vaccination')),
        ),
    ]
