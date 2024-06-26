# Generated by Django 5.0.6 on 2024-05-29 11:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10)),
                ('type', models.CharField(max_length=50)),
                ('price_per_night', models.DecimalField(decimal_places=2, max_digits=10)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='reservations.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('guest_name', models.CharField(max_length=255)),
                ('guest_email', models.EmailField(max_length=254)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='reservations.room')),
            ],
            options={
                'unique_together': {('room', 'check_in', 'check_out')},
            },
        ),
    ]
