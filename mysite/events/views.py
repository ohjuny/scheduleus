from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from twilio_sms import *

from .forms import *

# Create your views here.

def create(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save()
            event.users.add(request.user) 
            event.save()
            return HttpResponseRedirect(reverse("event", kwargs={'eventID': event.id}))
        else:
            return render(request, "create.html", {
                'form': form,
            })
    else:
        form = EventForm()
        return render(request, "create.html", {
            'form': form,
        })

def event(request, eventID):
    if request.method == "POST":
        user = User.objects.get(id = request.POST['user_id'])
        event = Event.objects.get(id = request.POST['event_id'])
        event.users.add(user)
        event.save()
        send_msg(str(user.profile.phone_number), event.end_datetime)
        return HttpResponseRedirect(reverse("event", kwargs={'eventID': event.id}))
    else:
        try:
            event = Event.objects.get(id=eventID)
        except:
            return render(request, "no_puzzle.html")
        return render(request, "event.html", {
            "event": event,
        })

def events(request):
    return render(request, "events.html", {
        "events": Event.objects.filter(users__username=request.user.username),
    })

def search_users(request):
    if request.is_ajax():
        search_text = request.GET.get('search_text')
        eventID = request.GET.get('eventID')
        event = Event.objects.get(id=eventID)
        users = User.objects.filter(username__icontains=search_text)
        for user in event.users.all():
            users = users.exclude(id=user.id)
        return render(request, "ajax_search_users.html", {
            'users': users,
            'search_len': len(search_text),
            'eventID': eventID,
        })