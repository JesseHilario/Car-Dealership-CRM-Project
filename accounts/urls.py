# from django.urls import path

# from .views import SignUpView


# urlpatterns = [
#     path("signup/", SignUpView.as_view(), name="signup"),
# ]
from django.urls import path

from .views import signup


urlpatterns = [
    path("signup/", signup, name="signup"),
]