# Generated by Django 2.2.5 on 2021-06-28 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Grandhospital_App', '0013_auto_20210628_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='dob',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='first_name',
            field=models.CharField(max_length=40),
        ),
    ]