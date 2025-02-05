# from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
# from django.urls import reverse_lazy
# from django.views.generic import CreateView


# class SignUpView(CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy("login")
#     template_name = "registration/signup.html"
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomSignupForm

def signup(request):
    if request.method == "POST":
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after signup
            return redirect('home')  # Redirect to homepage or dashboard
    else:
        form = CustomSignupForm()
    return render(request, "registration/signup.html", {"form": form})
