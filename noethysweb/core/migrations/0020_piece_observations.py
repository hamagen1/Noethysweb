# Generated by Django 3.2.7 on 2021-09-26 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20210925_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='piece',
            name='observations',
            field=models.TextField(blank=True, null=True, verbose_name='Observations'),
        ),
    ]
