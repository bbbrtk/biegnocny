# Generated by Django 2.0.7 on 2018-07-31 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baza', '0020_auto_20180731_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zaliczonypunkt',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
