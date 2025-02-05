from django.db import models


class AdditionalTaskScheduled(models.Model):
    appointment = models.OneToOneField('Appointment', models.DO_NOTHING, primary_key=True)  # The composite primary key (appointment_id, task_id) found, that is not supported. The first column is selected.
    task = models.ForeignKey('Task', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'additional_task_scheduled'
        unique_together = (('appointment', 'task'),)


class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    drop_off = models.DateTimeField(blank=True, null=True)
    pick_up = models.DateTimeField(blank=True, null=True)
    appointment_made_date = models.DateField(blank=True, null=True)
    customer = models.ForeignKey('Customer', models.DO_NOTHING, blank=True, null=True)
    time_slot = models.ForeignKey('TimeSlot', models.DO_NOTHING, blank=True, null=True)
    package = models.ForeignKey('Package', models.DO_NOTHING, blank=True, null=True)
    car = models.ForeignKey('Car', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'appointment'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Car(models.Model):
    car_id = models.AutoField(primary_key=True)
    interior = models.CharField(max_length=255, blank=True, null=True)
    odometer = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    vehicle = models.ForeignKey('VehicleType', models.DO_NOTHING, blank=True, null=True)
    license_plate_state = models.CharField(max_length=2, blank=True, null=True)
    license_plate = models.CharField(max_length=255, blank=True, null=True)
    cost = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    is_car_available = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'car'


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    f_name = models.CharField(max_length=255)
    m_init = models.CharField(max_length=1, blank=True, null=True)
    l_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10)
    email = models.CharField(max_length=255, blank=True, null=True)
    apt_number = models.CharField(max_length=255, blank=True, null=True)
    street_number = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'customer'
        unique_together = (('l_name', 'phone_number'),)


class CustomerCar(models.Model):
    customer = models.OneToOneField(Customer, models.DO_NOTHING, primary_key=True)  # The composite primary key (customer_id, car_id) found, that is not supported. The first column is selected.
    car = models.ForeignKey(Car, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'customer_car'
        unique_together = (('customer', 'car'),)


class CustomerPurchase(models.Model):
    customer = models.OneToOneField(Customer, models.DO_NOTHING, primary_key=True)  # The composite primary key (customer_id, purchase_id, car_id) found, that is not supported. The first column is selected.
    purchase = models.ForeignKey('Purchase', models.DO_NOTHING)
    car_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'customer_purchase'
        unique_together = (('customer', 'purchase', 'car_id'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Package(models.Model):
    package_id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    time_since_purchase = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'package'


class Part(models.Model):
    part_id = models.AutoField(primary_key=True)
    cost_of_part = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    task = models.ForeignKey('Task', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'part'


class PartReplaced(models.Model):
    appointment = models.OneToOneField(Appointment, models.DO_NOTHING, primary_key=True)  # The composite primary key (appointment_id, part_id) found, that is not supported. The first column is selected.
    part = models.ForeignKey(Part, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'part_replaced'
        unique_together = (('appointment', 'part'),)


class Purchase(models.Model):
    purchase_id = models.AutoField(primary_key=True)  # The composite primary key (purchase_id, car_id) found, that is not supported. The first column is selected.
    car = models.ForeignKey(Car, models.DO_NOTHING)
    date_of_purchase = models.DateField()
    sale_price = models.DecimalField(max_digits=11, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'purchase'
        unique_together = (('purchase_id', 'car'),)


class RequiredPartForTest(models.Model):
    test = models.OneToOneField('Task', models.DO_NOTHING, primary_key=True)  # The composite primary key (test_id, part_replacement_id) found, that is not supported. The first column is selected.
    part_replacement = models.ForeignKey('Task', models.DO_NOTHING, related_name='requiredpartfortest_part_replacement_set')

    class Meta:
        managed = False
        db_table = 'required_part_for_test'
        unique_together = (('test', 'part_replacement'),)


class Tally1(models.Model):
    n = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tally1'


class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    estd_time = models.DurationField(blank=True, null=True)
    estd_labor_cost = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    task_type = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'task'


class TaskPerformed(models.Model):
    appointment = models.OneToOneField(Appointment, models.DO_NOTHING, primary_key=True)  # The composite primary key (appointment_id, task_id) found, that is not supported. The first column is selected.
    task = models.ForeignKey(Task, models.DO_NOTHING)
    labor_cost = models.DecimalField(max_digits=9, decimal_places=2)
    time = models.DurationField()

    class Meta:
        managed = False
        db_table = 'task_performed'
        unique_together = (('appointment', 'task'),)


class TaskRecommended(models.Model):
    package = models.OneToOneField(Package, models.DO_NOTHING, primary_key=True)  # The composite primary key (package_id, task_id) found, that is not supported. The first column is selected.
    task = models.ForeignKey(Task, models.DO_NOTHING)
    is_mandatory = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'task_recommended'
        unique_together = (('package', 'task'),)


class TimeSlot(models.Model):
    time_slot_id = models.AutoField(primary_key=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'time_slot'


class VehiclePart(models.Model):
    part = models.OneToOneField(Part, models.DO_NOTHING, primary_key=True)  # The composite primary key (part_id, vehicle_id) found, that is not supported. The first column is selected.
    vehicle = models.ForeignKey('VehicleType', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'vehicle_part'
        unique_together = (('part', 'vehicle'),)


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
