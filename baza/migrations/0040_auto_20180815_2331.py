# Generated by Django 2.1 on 2018-08-15 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baza', '0039_zgloszenie_r_zgloszenie_w'),
    ]

    operations = [
        migrations.AddField(
            model_name='ekipa',
            name='punkt_startowy',
            field=models.ManyToManyField(blank=True, to='baza.Punkt_HS'),
        ),
        migrations.AddField(
            model_name='ekipa',
            name='punkty_bieg',
            field=models.ManyToManyField(blank=True, to='baza.Zgloszenie_HS'),
        ),
    ]
