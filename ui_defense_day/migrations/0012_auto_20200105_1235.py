# Generated by Django 2.2.6 on 2020-01-05 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui_defense_day', '0011_auto_20200105_0750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='job',
            field=models.CharField(blank=True, choices=[('student', 'Student'), ('industry', 'Industry'), ('professor', 'Professor'), ('presenter', 'Presenter'), ('admin', 'Admin')], default='student', max_length=11, null=True),
        ),
    ]
