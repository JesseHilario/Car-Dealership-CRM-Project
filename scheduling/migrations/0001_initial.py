# Generated by Django 5.1.4 on 2024-12-14 05:21

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drop_off', models.DateTimeField(default=django.utils.timezone.now)),
                ('pick_up', models.DateTimeField(default=django.utils.timezone.now)),
                ('appointment_made_date', models.DateField()),
            ],
        ),
    ]
