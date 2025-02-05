from django.urls import path
from . import views


app_name = 'carsale'
urlpatterns = [
    path('',    # first arg we specify url endpoint; empty string represents root of this app
        views.index,
        name='index'),   # best practice, we should name these url endpoints
    path('<int:car_id>', views.detail, name='detail'),
    path('purchase/<int:car_id>',views.purchase,name='purchase')
]