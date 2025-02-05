from django.shortcuts import render
from .models import Car
from django.shortcuts import render
from django.db import connection
from .forms import DateRangeForm

def sale_statistics(request):
    sale_statistics_data = None
    start_date = None
    end_date = None
    
    if request.method == 'POST':
        form = DateRangeForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']

            # Call the PostgreSQL function with the date range parameters
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT * FROM get_sale_statistics_by_date_range(%s, %s);
                """, [start_date, end_date])
                sale_statistics_data = cursor.fetchall()

    else:
        form = DateRangeForm()

    return render(request, 'salestats/sale_statistics.html', {
        'form': form,
        'sale_statistics_data': sale_statistics_data,
        'start_date': start_date,
        'end_date': end_date
    })

# Create your views here.
def index(request):     # 'request' is arbitrary, but the object that is passed is an http object (?). See urls.py for url mappings
    car = Car.objects.filter(is_car_available='True')
    return render(
        request,
        'carsale/index.html',        # name of our template
        {'car':car}    # optional context object, a dictionary to pass data to our template
    )
