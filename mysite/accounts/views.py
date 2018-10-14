from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import dateutil.parser as p

from .forms import *
from .models import *

import quickstart

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user, Profile = form.save()
            user.save()
            user.profile.save()

            arr = quickstart.main()
            print(arr)
            for obj in arr:
                newTimeSlot = TimeSlot(profile=user.profile, datetime=p.parse(obj))
                newTimeSlot.save()

            login(request, user)
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