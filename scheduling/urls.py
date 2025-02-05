from django.urls import path
from . import views     # we use relative import statement bc django is like that

# passes the url patterns django will be expecting in list object
# for instance, 
# servicesscheduling/
# servicesscheduling/1/details
# we refer to this as a url configuration; every app should have one
app_name = 'cars'
urlpatterns = [
    path('',    # first arg we specify url endpoint; empty string represents root of this app
        views.index,    # second arg is a reference to the view function. Notice we are not calling the function, django will call and give it an http request object
        name='index'),   # best practice, we should name these url endpoints
    path('<int:car_id>', views.detail, name='detail')
]