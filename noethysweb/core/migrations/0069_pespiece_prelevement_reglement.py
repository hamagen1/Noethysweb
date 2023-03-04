# Generated by Django 3.2.11 on 2023-03-03 23:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0068_auto_20230221_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='pespiece',
            name='prelevement_reglement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.reglement', verbose_name='Règlement'),
        ),
    ]
