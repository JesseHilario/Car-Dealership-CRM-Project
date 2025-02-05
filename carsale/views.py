from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import connection
from .models import Car, Customer
from .forms import PurchaseTransactionForm


def index(request):     # 'request' is arbitrary, but the object that is passed is an http object (?). See urls.py for url mappings
    car = Car.objects.filter(is_car_available='True')
    return render(
        request,
        'carsale/index.html',        # name of our template
        {'car':car}    # optional context object, a dictionary to pass data to our template
    )

def detail(request, car_id):
    # try:
    #     vehicle_type = VehicleType.objects.get(pk=vehicle_id)
    #     return render(request, 'carsale/detail.html', {'vehicle_type':vehicle_type})
    # except VehicleType.DoesNotExist:
    #     raise Http404()
    # vehicle_type = get_object_or_404(VehicleType, pk=vehicle_id)
    
    car = get_object_or_404(Car, pk=car_id)
    return render(request, 'carsale/detail.html', {'car':car})

@login_required()
def purchase(request, car_id):
    car = get_object_or_404(Car, pk=car_id)

    # Ensure user is linked to a Customer record
    try:
        customer = Customer.objects.get(l_name=request.user.last_name, phone_number=request.user.email)   # user.email is actually the phone number
    except Customer.DoesNotExist:
        messages.error(request, "Customer not found. Please update your profile.")
        return redirect("carsale:index")  # Redirect to the home page instead of rendering an error page

    if request.method == "POST":
        form = PurchaseTransactionForm(request.POST, user=request.user, car=car)
        if form.is_valid():
            data = form.cleaned_data
            customer_id = data["customer_id"]
            car_id = data["car_id"]
            date_of_purchase = data["date_of_purchase"]
            sale_price = data["sale_price"]
            license_plate_state = data["license_plate_state"]
            license_plate = data["license_plate"]

            with connection.cursor() as cursor:
                cursor.execute(
                    "CALL make_new_purchase_transaction(%s, %s, %s, %s, %s, %s)",
                    [car_id, customer_id, date_of_purchase, sale_price, license_plate_state, license_plate]
                )

            messages.success(request, "Transaction successful! Your purchase has been completed.")
            return redirect('carsale:index')  # Redirect to a confirmation page
    else:
        form = PurchaseTransactionForm(user=request.user, car=car)

    return render(request, "carsale/purchase.html", {"form": form, "car": car})