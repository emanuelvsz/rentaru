# Generated by Django 4.2.6 on 2023-11-24 20:03

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('cpf', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('duration', models.CharField()),
                ('release_date', models.DateField()),
                ('director', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=50)),
                ('language', models.CharField(max_length=50)),
                ('cover_image', models.URLField()),
                ('trailer_url', models.URLField(blank=True, null=True)),
                ('rental_price', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='MovieRental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rented_at', models.DateField()),
                ('payment_type', models.CharField(max_length=255)),
                ('price', models.FloatField(default=0)),
                ('client_id', models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, to='product.client')),
                ('movie_id', models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, to='product.movie')),
            ],
        ),
    ]
