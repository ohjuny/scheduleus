from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import ../../twilio as twilio

from .forms import *

# Create your views here.

def create(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save()
            event.users.add(request.user)
            # return render(request, "home.html")
            return HttpResponseRedirect(reverse("event", kwargs={'eventID': event.id}))
        else:
            return render(request, "create.html", {
                'form': form,
            })

        #loop through users
        twilio.send_msg() #string number, datetime lasttime
    else:
        form = EventForm()
        return render(request, "create.html", {
            'form': form,
        })

def event(request, eventID):
    try:
        event = Event.objects.get(id=eventID)
    except:
        return render(request, "no_puzzle.html")
    return render(request, "event.html", {
        "event": event,
    })

def events(request):
    return render(request, "events.html", {
        "events": Event.objects.all(),
    })

def search_users(request):
    if request.is_ajax():
        search_text = request.GET.get('search_text')
        eventID = request.GET.get('eventID')
        # event = Event.objects.filter(eventID=eventID)
        # users = User.objects.filter(username__icontains=search_text),
        # for user in users:
        #     if user in event.users:
        #         User.objects.exclude(userID=user.id)
        return render(request, "ajax_search_users.html", {
            'users': users,
            'search_len': len(search_text),
        })