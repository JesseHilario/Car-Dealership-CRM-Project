from django.urls import path
from . import views


app_name = 'salestats'
urlpatterns = [
    # path('',    # first arg we specify url endpoint; empty string represents root of this app
    #     views.index,
    #     name='index'),
    path('', views.sale_statistics, name='sale_statistics'),
]