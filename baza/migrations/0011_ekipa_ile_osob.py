# Generated by Django 2.0.7 on 2018-07-29 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baza', '0010_auto_20180729_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='ekipa',
            name='ile_osob',
            field=models.IntegerField(default=0),
        ),
    ]
