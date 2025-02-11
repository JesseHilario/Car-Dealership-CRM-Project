# Generated by Django 5.1.4 on 2025-01-27 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('car_id', models.AutoField(primary_key=True, serialize=False)),
                ('interior', models.CharField(blank=True, max_length=255, null=True)),
                ('odometer', models.CharField(blank=True, max_length=255, null=True)),
                ('color', models.CharField(blank=True, max_length=255, null=True)),
                ('license_plate_state', models.CharField(blank=True, max_length=2, null=True)),
                ('license_plate', models.CharField(blank=True, max_length=255, null=True)),
                ('cost', models.DecimalField(blank=True, decimal_places=2, max_digits=11, null=True)),
                ('is_car_available', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'db_table': 'car',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('f_name', models.CharField(max_length=255)),
                ('m_init', models.CharField(blank=True, max_length=1, null=True)),
                ('l_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=10)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('apt_number', models.CharField(blank=True, max_length=255, null=True)),
                ('street_number', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'customer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CustomerCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'customer_car',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CustomerPurchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'customer_purchase',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('purchase_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_of_purchase', models.DateField()),
                ('sale_price', models.DecimalField(decimal_places=2, max_digits=11)),
            ],
            options={
                'db_table': 'purchase',
                'managed': False,
            },
        ),
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
    ]
