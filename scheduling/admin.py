from django.contrib import admin
from .models import VehicleType

class VehicleTypeAdmin(admin.ModelAdmin):
    list_display = ('make','model','year','tire_type')

admin.site.register(VehicleType, VehicleTypeAdmin)