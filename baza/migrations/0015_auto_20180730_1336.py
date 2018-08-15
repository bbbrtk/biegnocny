# Generated by Django 2.0.7 on 2018-07-30 11:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baza', '0014_auto_20180730_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dostep',
            field=models.CharField(blank=True, choices=[('PK', 'PunktyKwadraty'), ('UE', 'UczestnicyEkipy'), ('W', 'Wszystko')], default='PK', max_length=2),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
