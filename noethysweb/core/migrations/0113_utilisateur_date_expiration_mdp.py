# Generated by Django 3.2.11 on 2023-05-01 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0112_alter_modeleemail_categorie'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilisateur',
            name='date_expiration_mdp',
            field=models.DateTimeField(blank=True, null=True, verbose_name="Date d'expiration du mot de passe"),
        ),
    ]
