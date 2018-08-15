# Generated by Django 2.1 on 2018-08-15 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baza', '0030_auto_20180801_1145'),
    ]

    operations = [
        migrations.CreateModel(
            name='Punkt_HS',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('numer', models.IntegerField(default=0)),
                ('kod', models.CharField(blank=True, max_length=3)),
                ('nazwa', models.CharField(blank=True, max_length=128)),
                ('skrzyzowanie', models.CharField(blank=True, max_length=128)),
                ('adres', models.CharField(blank=True, max_length=128)),
                ('opis_zawieszenia_1', models.CharField(blank=True, max_length=256)),
                ('opis_zawieszenia_2', models.CharField(blank=True, max_length=256)),
                ('opis', models.CharField(blank=True, max_length=1024)),
                ('pytanie', models.CharField(blank=True, max_length=256)),
                ('odpowiedz', models.CharField(blank=True, max_length=256)),
                ('dojscie', models.CharField(blank=True, max_length=256)),
                ('punktowy', models.CharField(blank=True, max_length=64)),
                ('uwagi', models.CharField(blank=True, max_length=256)),
            ],
            options={
                'ordering': ('numer',),
            },
        ),
        migrations.CreateModel(
            name='Zgloszenie_HS',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('podpowiedz', models.BooleanField(default=False)),
                ('zawieszenie', models.BooleanField(default=False)),
                ('brak_punktu', models.BooleanField(default=False)),
                ('uwagi', models.CharField(blank=True, max_length=256)),
                ('punkt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baza.Punkt_HS')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]