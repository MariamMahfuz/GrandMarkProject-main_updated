# Generated by Django 2.2.5 on 2021-06-28 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Grandhospital_App', '0004_auto_20210628_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], default='Gender', max_length=10),
        ),
    ]