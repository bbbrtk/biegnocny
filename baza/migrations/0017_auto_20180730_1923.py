# Generated by Django 2.0.7 on 2018-07-30 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baza', '0016_auto_20180730_1445'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'permissions': (('WidokGlowny', 'Dostęp do strony głównej'), ('Punkty', 'Wyświetlanie punktów'), ('Kwadraty', 'Wyświetlanie kwadratów'), ('Ekipy', 'Wyświetlanie szczegółów ekip'), ('Uczestnicy', 'Wyświetlanie uczestników'))},
        ),
        migrations.RemoveField(
            model_name='profile',
            name='dostep',
        ),
    ]
