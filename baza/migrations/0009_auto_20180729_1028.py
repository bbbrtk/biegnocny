# Generated by Django 2.0.7 on 2018-07-29 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baza', '0008_ekipa_weryfikacja_zgod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uczestnik',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
