from django.contrib import admin
from .models import Customer, VehicleType, Car, Purchase, CustomerCar, CustomerPurchase

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_id','f_name','m_init','l_name','phone_number','email','apt_number','street_number','city')

class VehicleTypeAdmin(admin.ModelAdmin):
    list_display = ('vehicle_id','make','model','year','tire_type','engine_type')

class CarAdmin(admin.ModelAdmin):
    list_display = ('car_id','interior','odometer','color','vehicle','license_plate_state','cost','is_car_available')

admin.site.register(Customer, CustomerAdmin)
admin.site.register(VehicleType, VehicleTypeAdmin)
admin.site.register(Car, CarAdmin)

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('purchase_id','car','date_of_purchase','sale_price')

admin.site.register(Purchase, PurchaseAdmin)

class CustomerCarAdmin(admin.ModelAdmin):
    list_display = ('customer','car')

admin.site.register(CustomerCar, CustomerCarAdmin)

class CustomerPurchaseAdmin(admin.ModelAdmin):
    list_display = ('customer','purchase','car_id')

admin.site.register(CustomerPurchase, CustomerPurchaseAdmin)