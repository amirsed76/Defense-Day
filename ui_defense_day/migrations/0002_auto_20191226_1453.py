# Generated by Django 2.2 on 2019-12-26 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui_defense_day', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('student', 'Student'), ('presenter', 'Presenter'), ('industry', 'Industry'), ('supervisor', 'Supervisor'), ('referee', 'Referee'), ('admin', 'Admin')], max_length=20),
        ),
    ]