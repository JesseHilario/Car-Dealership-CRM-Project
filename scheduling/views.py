from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404     # used to render a template
from .models import VehicleType, Car

# Create your views here.
# view functions take requests and return responses
def index(request):     # 'request' is arbitrary, but the object that is passed is an http object (?). See urls.py for url mappings
    car = Car.objects.filter(is_car_available='True')    # SELECT * FROM scheduling_scheduling
    # Appointment.objects.filter(appointment_made_date='12-11-2024')    # SELECT * FROM scheduling_scheduling WHERE
    # Appointment.objects.get(id=1)     # SELECT FROM scheduling_scheduling WHERE id=1
    # output = ', '.join([(a.drop_off, a.pick_up) for a in appointments])   # don't need this because of render function
    return render(
        request,
        'scheduling/index.html',        # name of our template
        {'car':car}    # optional context object, a dictionary to pass data to our template
    )
    # return HttpResponse("Hello, world.")

def detail(request, car_id):
    # try:
    #     vehicle_type = VehicleType.objects.get(pk=vehicle_id)
    #     return render(request, 'scheduling/detail.html', {'vehicle_type':vehicle_type})
    # except VehicleType.DoesNotExist:
    #     raise Http404()
    # vehicle_type = get_object_or_404(VehicleType, pk=vehicle_id)
    
    car = get_object_or_404(Car, pk=car_id)
    return render(request, 'scheduling/detail.html', {'car':car})