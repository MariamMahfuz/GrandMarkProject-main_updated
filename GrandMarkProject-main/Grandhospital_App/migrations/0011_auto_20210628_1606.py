# Generated by Django 2.2.5 on 2021-06-28 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Grandhospital_App', '0010_auto_20210628_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='dob',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]