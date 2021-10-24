# Generated by Django 4.0a1 on 2021-10-04 10:25

from django.db import migrations, models
import django_cryptography.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_piece_auteur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adressemail',
            name='adresse',
            field=django_cryptography.fields.encrypt(models.EmailField(help_text="Saisissez l'adresse mail utilisée.", max_length=300, verbose_name="Adresse d'envoi")),
        ),
        migrations.AlterField(
            model_name='adressemail',
            name='hote',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, help_text="Saisissez le nom de l'hôte de la messagerie (Ex: smtp.orange.fr, smtp.gmail.com...).", max_length=300, null=True, verbose_name='Hôte')),
        ),
        migrations.AlterField(
            model_name='adressemail',
            name='motdepasse',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, help_text='Saisissez le mot de passe de la messagerie.', max_length=300, null=True, verbose_name='Mot de passe')),
        ),
        migrations.AlterField(
            model_name='adressemail',
            name='utilisateur',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, help_text="Saisissez le nom d'utilisateur (Souvent identique à l'adresse mail).", max_length=300, null=True, verbose_name='Utilisateur')),
        ),
        migrations.AlterField(
            model_name='assurance',
            name='num_contrat',
            field=django_cryptography.fields.encrypt(models.CharField(max_length=200, verbose_name='N° de contrat')),
        ),
        migrations.AlterField(
            model_name='comptebancaire',
            name='code_ics',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=200, null=True, verbose_name='Code ICS')),
        ),
        migrations.AlterField(
            model_name='comptebancaire',
            name='numero',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=200, null=True, verbose_name='Numéro')),
        ),
        migrations.AlterField(
            model_name='contact',
            name='cp_resid',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=50, null=True, verbose_name='Code postal')),
        ),
        migrations.AlterField(
            model_name='contact',
            name='mail',
            field=django_cryptography.fields.encrypt(models.EmailField(blank=True, max_length=300, null=True, verbose_name='Email')),
        ),
        migrations.AlterField(
            model_name='contact',
            name='rue_resid',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=200, null=True, verbose_name='Rue')),
        ),
        migrations.AlterField(
            model_name='contact',
            name='tel_domicile',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=100, null=True, verbose_name='Tél domicile')),
        ),
        migrations.AlterField(
            model_name='contact',
            name='tel_mobile',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=100, null=True, verbose_name='Tél portable')),
        ),
        migrations.AlterField(
            model_name='contact',
            name='ville_resid',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=200, null=True, verbose_name='Ville')),
        ),
        migrations.AlterField(
            model_name='contacturgence',
            name='cp_resid',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=50, null=True, verbose_name='Code postal')),
        ),
        migrations.AlterField(
            model_name='contacturgence',
            name='lien',
            field=django_cryptography.fields.encrypt(models.CharField(max_length=200, verbose_name="Lien avec l'individu")),
        ),
        migrations.AlterField(
            model_name='contacturgence',
            name='mail',
            field=django_cryptography.fields.encrypt(models.EmailField(blank=True, max_length=300, null=True, verbose_name='Email')),
        ),
        migrations.AlterField(
            model_name='contacturgence',
            name='observations',
            field=django_cryptography.fields.encrypt(models.TextField(blank=True, null=True, verbose_name='Observations')),
        ),
        migrations.AlterField(
            model_name='contacturgence',
            name='rue_resid',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=200, null=True, verbose_name='Rue')),
        ),
        migrations.AlterField(
            model_name='contacturgence',
            name='tel_domicile',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=100, null=True, verbose_name='Tél domicile')),
        ),
        migrations.AlterField(
            model_name='contacturgence',
            name='tel_mobile',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=100, null=True, verbose_name='Tél portable')),
        ),
        migrations.AlterField(
            model_name='contacturgence',
            name='tel_travail',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=100, null=True, verbose_name='Tél travail')),
        ),
        migrations.AlterField(
            model_name='contacturgence',
            name='ville_resid',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=200, null=True, verbose_name='Ville')),
        ),
        migrations.AlterField(
            model_name='destinataire',
            name='adresse',
            field=django_cryptography.fields.encrypt(models.EmailField(blank=True, max_length=300, null=True, verbose_name='Email')),
        ),
        migrations.AlterField(
            model_name='famille',
            name='cp_resid',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=50, null=True, verbose_name='Code postal')),
        ),
        migrations.AlterField(
            model_name='famille',
            name='mail',
            field=django_cryptography.fields.encrypt(models.EmailField(blank=True, max_length=300, null=True, verbose_name='Email favori')),
        ),
        migrations.AlterField(
            model_name='famille',
            name='num_allocataire',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=100, null=True, verbose_name="Numéro d'allocataire")),
        ),
        migrations.AlterField(
            model_name='famille',
            name='rue_resid',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=200, null=True, verbose_name='Rue')),
        ),
        migrations.AlterField(
            model_name='famille',
            name='ville_resid',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=200, null=True, verbose_name='Ville')),
        ),
        migrations.AlterField(
            model_name='historique',
            name='detail',
            field=django_cryptography.fields.encrypt(models.TextField(blank=True, null=True, verbose_name='Détail')),
        ),
        migrations.AlterField(
            model_name='individu',
            name='annee_deces',
            field=django_cryptography.fields.encrypt(models.IntegerField(blank=True, null=True, verbose_name='Année de décès')),
        ),
        migrations.AlterField(
            model_name='individu',
            name='cp_naiss',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=50, null=True, verbose_name='Code postal')),
        ),
        migrations.AlterField(
            model_name='individu',
            name='cp_resid',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=50, null=True, verbose_name='Code postal')),
        ),
        migrations.AlterField(
            model_name='individu',
            name='date_naiss',
            field=django_cryptography.fields.encrypt(models.DateField(blank=True, null=True, verbose_name='Date de naissance')),
        ),
        migrations.AlterField(
            model_name='individu',
            name='employeur',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=200, null=True, verbose_name='Employeur')),
        ),
        migrations.AlterField(
            model_name='individu',
            name='mail',
            field=django_cryptography.fields.encrypt(models.EmailField(blank=True, max_length=300, null=True, verbose_name='Email personnel')),
        ),
        migrations.AlterField(
            model_name='individu',
            name='profession',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=200, null=True, verbose_name='Profession')),
        ),
        migrations.AlterField(
            model_name='individu',
            name='rue_resid',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=200, null=True, verbose_name='Rue')),
        ),
        migrations.AlterField(
            model_name='individu',
            name='tel_domicile',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=100, null=True, verbose_name='Tél domicile')),
        ),
        migrations.AlterField(
            model_name='individu',
            name='tel_fax',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=100, null=True, verbose_name='Fax personnel')),
        ),
        migrations.AlterField(
            model_name='individu',
            name='tel_mobile',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=100, null=True, verbose_name='Tél portable')),
        ),
        migrations.AlterField(
            model_name='individu',
            name='travail_fax',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=100, null=True, verbose_name='Fax pro.')),
        ),
        migrations.AlterField(
            model_name='individu',
            name='travail_mail',
            field=django_cryptography.fields.encrypt(models.EmailField(blank=True, max_length=300, null=True, verbose_name='Email pro.')),
        ),
        migrations.AlterField(
            model_name='individu',
            name='travail_tel',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=100, null=True, verbose_name='Téléphone pro.')),
        ),
        migrations.AlterField(
            model_name='individu',
            name='ville_naiss',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=200, null=True, verbose_name='Ville')),
        ),
        migrations.AlterField(
            model_name='individu',
            name='ville_resid',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=200, null=True, verbose_name='Ville')),
        ),
        migrations.AlterField(
            model_name='mandat',
            name='individu_cp',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=50, null=True, verbose_name='Code postal')),
        ),
        migrations.AlterField(
            model_name='mandat',
            name='individu_rue',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=200, null=True, verbose_name='Rue')),
        ),
        migrations.AlterField(
            model_name='mandat',
            name='individu_ville',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=200, null=True, verbose_name='Ville')),
        ),
        migrations.AlterField(
            model_name='portailrenseignement',
            name='valeur',
            field=django_cryptography.fields.encrypt(models.TextField(blank=True, null=True, verbose_name='Valeur')),
        ),
        migrations.AlterField(
            model_name='quotient',
            name='observations',
            field=django_cryptography.fields.encrypt(models.TextField(blank=True, null=True, verbose_name='Observations')),
        ),
        migrations.AlterField(
            model_name='quotient',
            name='quotient',
            field=django_cryptography.fields.encrypt(models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True, verbose_name='Quotient')),
        ),
        migrations.AlterField(
            model_name='quotient',
            name='revenu',
            field=django_cryptography.fields.encrypt(models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True, verbose_name='Revenu')),
        ),
        migrations.AlterField(
            model_name='unite',
            name='incompatibilites',
            field=models.ManyToManyField(blank=True, to='core.Unite', verbose_name='Incompatibilités'),
        ),
    ]