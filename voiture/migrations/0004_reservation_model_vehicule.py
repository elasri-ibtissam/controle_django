# Generated by Django 4.1.7 on 2023-05-03 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voiture', '0003_remove_reservation_nbr_place_reservation_adresse_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='model_vehicule',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
