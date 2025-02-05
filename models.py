# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    f_name = models.CharField(max_length=255)
    m_init = models.CharField(max_length=1, blank=True, null=True)
    l_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=254, blank=True, null=True)
    apt_number = models.CharField(max_length=255, blank=True, null=True)
    street_number = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'customer'
        unique_together = (('l_name', 'phone_number'),)

class Package(models.Model):
    package_id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    time_since_purchase = models.IntegerField(blank=True, null=True)
    packages_recommend_task = models.ManyToManyField(
        "Task",
        through="TaskRecommended",
        through_fields=("package","task")
    )

    class Meta:
        managed = False
        db_table = 'package'

class TimeSlot(models.Model):
    time_slot_id = models.AutoField(primary_key=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'time_slot'

class VehicleType(models.Model):
    vehicle_id = models.AutoField(primary_key=True)
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.IntegerField()
    tire_type = models.CharField(max_length=255, blank=True, null=True)
    engine_type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vehicle_type'
        unique_together = (('make', 'model', 'year', 'tire_type', 'engine_type'),)

class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    estd_time = models.DurationField(blank=True, null=True)
    estd_labor_cost = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    task_type = models.CharField(max_length=4, blank=True, null=True)
    appointments_task_performed = models.ManyToManyField(
        "Appointment",
        through="TaskPerformed",
        through_fields=("task","appointment")
    )
    appointments_task_scheduled = models.ManyToManyField(
        "Appointment",
        through="AdditionalTaskScheduled",
        through_fields=("task","appointment")
    )

    class Meta:
        managed = False
        db_table = 'task'


class Car(models.Model):
    car_id = models.AutoField(primary_key=True)
    interior = models.CharField(max_length=255, blank=True, null=True)
    odometer = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    vehicle = models.ForeignKey('VehicleType', on_delete=models.PROTECT, blank=True, null=True)
    license_plate_state = models.CharField(max_length=2, blank=True, null=True)
    license_plate = models.CharField(max_length=255, blank=True, null=True)
    cost = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    is_car_available = models.BooleanField(blank=True, null=True)
    customers_car = models.ManyToManyField(
        "Customer",
        through="CustomerCar",
        through_fields=("car", "customer"))

    class Meta:
        managed = False
        db_table = 'car'

class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    drop_off = models.DateTimeField(blank=True, null=True)
    pick_up = models.DateTimeField(blank=True, null=True)
    appointment_made_date = models.DateField(blank=True, null=True)
    customer = models.ForeignKey('Customer', on_delete=models.PROTECT, blank=True, null=True)
    time_slot = models.ForeignKey('TimeSlot', on_delete=models.CASCADE, blank=True, null=True)
    package = models.ForeignKey('Package', on_delete=models.PROTECT, blank=True, null=True)
    car = models.ForeignKey('Car', on_delete=models.PROTECT, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'appointment'

class Part(models.Model):
    part_id = models.AutoField(primary_key=True)
    cost_of_part = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    task = models.ForeignKey('Task', on_delete=models.PROTECT, blank=True, null=True)
    appointments_part = models.ManyToManyField(
        "Appointment",
        through="PartReplaced",
        through_fields=("part","appointment")
    )
    vehicles_part = models.ManyToManyField(
        "VehicleType",
        through="VehiclePart",
        through_fields=("part","vehicle")
    )

    class Meta:
        managed = False
        db_table = 'part'

class Purchase(models.Model):
    purchase_id = models.AutoField(primary_key=True)  # The composite primary key (purchase_id, car_id) found, that is not supported. The first column is selected.
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_of_purchase = models.DateField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)
    customers_purchase = models.ManyToManyField(
        "Customer",
        through="CustomerPurchase",
        through_fields=("purchase","customer")
    )

    class Meta:
        managed = False
        db_table = 'purchase'
        unique_together = (('purchase_id', 'car'),)

class CustomerCar(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    car = models.ForeignKey(Car, models.PROTECT)

    class Meta:
        managed = False
        db_table = 'customer_car'
        unique_together = (('customer', 'car'),)

class CustomerPurchase(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    purchase = models.ForeignKey('Purchase', on_delete=models.CASCADE)
    car_id = models.ForeignKey('Car',on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'customer_purchase'
        unique_together = (('customer', 'purchase', 'car_id'),)

class PartReplaced(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    part = models.ForeignKey(Part, on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'part_replaced'
        unique_together = (('appointment', 'part'),)

class TaskPerformed(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE) 
    task = models.ForeignKey(Task, on_delete=models.PROTECT)
    labor_cost = models.DecimalField(max_digits=9, decimal_places=2)
    time = models.DurationField()

    class Meta:
        managed = False
        db_table = 'task_performed'
        unique_together = (('appointment', 'task'),)

class AdditionalTaskScheduled(models.Model):
    appointment = models.ForeignKey('Appointment', on_delete=models.CASCADE)
    task = models.ForeignKey('Task', on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'additional_task_scheduled'
        unique_together = (('appointment', 'task'),)

class TaskRecommended(models.Model):
    package = models.ForeignKey(Package, on_delete=models.PROTECT)
    task = models.ForeignKey(Task, on_delete=models.PROTECT)
    is_mandatory = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'task_recommended'
        unique_together = (('package', 'task'),)

class RequiredPartForTest(models.Model):
    test = models.ForeignKey('Task', on_delete=models.PROTECT)
    part_replacement = models.ForeignKey('Task', on_delete=models.PROTECT, related_name='requiredpartfortest_part_replacement_set')

    class Meta:
        managed = False
        db_table = 'required_part_for_test'
        unique_together = (('test', 'part_replacement'),)

class VehiclePart(models.Model):
    part = models.ForeignKey(Part, on_delete=models.PROTECT)
    vehicle = models.ForeignKey('VehicleType', on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'vehicle_part'
        unique_together = (('part', 'vehicle'),)

class Tally1(models.Model):
    n = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tally1'
