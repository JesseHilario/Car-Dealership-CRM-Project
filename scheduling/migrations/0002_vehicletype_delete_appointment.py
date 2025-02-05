# Generated by Django 5.1.4 on 2025-01-23 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduling', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleType',
            fields=[
                ('vehicle_id', models.AutoField(primary_key=True, serialize=False)),
                ('make', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('tire_type', models.CharField(blank=True, max_length=255, null=True)),
                ('engine_type', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'vehicle_type',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Appointment',
        ),
    ]
