# Generated by Django 2.2.5 on 2021-06-28 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Grandhospital_App', '0006_auto_20210628_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='appointment_candidate_pics'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='zipcode',
            field=models.IntegerField(blank=True, max_length=10),
        ),
    ]