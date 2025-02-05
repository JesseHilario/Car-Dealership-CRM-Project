from django.db import models    # django.db encapsulates all functionality working with databases
from django.utils import timezone

# class Appointment(models.Model):
#     drop_off = models.DateTimeField(default=timezone.now)   # don't call timezone.now otherwise current datetime will be hardcoded (THIS COULD BE USEFUL?? FOR WHEN THE DEALER MARKS AS PRESENT THE CUSTOMER. wait nvm bc it's gonna be default until there's another migration)
#     pick_up = models.DateTimeField(default=timezone.now)
#     appointment_made_date = models.DateField()

#     def __str__(self):
#         return self.drop_off

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
    # customers_car = models.ManyToManyField(
    #     "Customer",
    #     through="CustomerCar",
    #     through_fields=("car", "customer"))

    class Meta:
        managed = False
        db_table = 'car'