# Generated by Django 3.2.11 on 2023-03-06 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0074_tarifproduit'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarifproduit',
            name='label_prestation',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Label de la prestation'),
        ),
    ]
