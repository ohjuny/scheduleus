from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .forms import *
from .models import *

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user, Profile = form.save()
            user.save()
            user.profile.save()

            return render(request, "home.html")
        else:
            return render(request, "signup.html", {
                'form': form,
            })
    else:
        form = UserForm()
        return render(request, "signup.html", {
            'form': form,
        })