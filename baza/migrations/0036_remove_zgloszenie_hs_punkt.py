# Generated by Django 2.1 on 2018-08-15 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baza', '0035_auto_20180815_2301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zgloszenie_hs',
            name='punkt',
        ),
    ]
