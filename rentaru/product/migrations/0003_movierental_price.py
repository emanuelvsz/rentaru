# Generated by Django 4.2.6 on 2023-11-24 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_movie_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='movierental',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
