# Generated by Django 3.2.11 on 2023-02-05 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0066_unite_dependances'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unite',
            name='dependances',
            field=models.ManyToManyField(blank=True, to='core.Unite', verbose_name='Dépendances'),
        ),
    ]