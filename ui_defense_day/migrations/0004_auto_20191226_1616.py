# Generated by Django 2.2 on 2019-12-26 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui_defense_day', '0003_presenter_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presenter',
            name='score',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
    ]
