# Generated by Django 2.0.7 on 2018-07-27 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baza', '0003_auto_20180727_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ekipa',
            name='pozostalo',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='uczestnik',
            name='uwagi',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]