# Generated by Django 2.0.7 on 2018-08-01 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baza', '0029_auto_20180731_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='punkt',
            name='dojscie',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name='punkt',
            name='kod',
            field=models.CharField(blank=True, max_length=3),
        ),
        migrations.AddField(
            model_name='punkt',
            name='opis',
            field=models.CharField(blank=True, max_length=1024),
        ),
    ]
