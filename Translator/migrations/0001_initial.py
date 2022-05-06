# Generated by Django 3.1.5 on 2022-04-23 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LANGUAGE_CODE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Number', models.IntegerField()),
                ('Letters_Alef', models.CharField(max_length=2)),
                ('Letters_Be', models.CharField(max_length=2)),
                ('Letters_Pe', models.CharField(max_length=2)),
                ('Letters_Te', models.CharField(max_length=2)),
                ('Letters_Se', models.CharField(max_length=2)),
                ('Letters_Jim', models.CharField(max_length=2)),
                ('Letters_Che', models.CharField(max_length=2)),
                ('Letters_Khe', models.CharField(max_length=2)),
                ('Letters_Dal', models.CharField(max_length=2)),
                ('Letters_Zal', models.CharField(max_length=2)),
                ('Letters_Re', models.CharField(max_length=2)),
                ('Letters_Ze', models.CharField(max_length=2)),
                ('Letters_Zhe', models.CharField(max_length=2)),
                ('Letters_Sin', models.CharField(max_length=2)),
                ('Letters_Shin', models.CharField(max_length=2)),
                ('Letters_Sad', models.CharField(max_length=2)),
                ('Letters_Zad', models.CharField(max_length=2)),
                ('Letters_Ta', models.CharField(max_length=2)),
                ('Letters_Za', models.CharField(max_length=2)),
                ('Letters_Ain', models.CharField(max_length=2)),
                ('Letters_Ghain', models.CharField(max_length=2)),
                ('Letters_Fe', models.CharField(max_length=2)),
                ('Letters_Kaf', models.CharField(max_length=2)),
                ('Letters_Ghaf', models.CharField(max_length=2)),
                ('Letters_Lam', models.CharField(max_length=2)),
                ('Letters_MiM', models.CharField(max_length=2)),
                ('Letters_Noon', models.CharField(max_length=2)),
                ('Letters_Vav', models.CharField(max_length=2)),
                ('Letters_He', models.CharField(max_length=2)),
                ('Letters_Ye', models.CharField(max_length=2)),
                ('Letters_Hyphen', models.CharField(max_length=2)),
            ],
        ),
    ]
