# Generated by Django 2.2 on 2019-12-26 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui_defense_day', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='presenter',
            name='file2',
            field=models.FileField(blank=True, null=True, upload_to='document/'),
        ),
    ]