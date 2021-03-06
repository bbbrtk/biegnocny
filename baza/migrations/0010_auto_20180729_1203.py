# Generated by Django 2.0.7 on 2018-07-29 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baza', '0009_auto_20180729_1028'),
    ]

    operations = [
        migrations.CreateModel(
            name='Termin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('termin', models.CharField(max_length=64)),
                ('kwota', models.FloatField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='ekipa',
            name='termin_wplat',
        ),
        migrations.AlterField(
            model_name='ekipa',
            name='uwagi',
            field=models.CharField(blank=True, default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='uczestnik',
            name='uwagi',
            field=models.CharField(blank=True, default='', max_length=256),
        ),
        migrations.AddField(
            model_name='ekipa',
            name='termin_wplat',
            field=models.ManyToManyField(to='baza.Termin'),
        ),
    ]
