import os

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from twilio_sms import *

from .forms import *

from twilio import rest
from twilio.twiml import messaging_response, voice_response

# [START configuration]
TWILIO_ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
TWILIO_NUMBER = os.environ['TWILIO_NUMBER']
# [END configuration]


# Create your views here.

def create(request):
    if request.method == "POST":
        print ('created event')
        client = rest.Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        rv = client.messages.create(
            to="+19495454049",
            from_=TWILIO_NUMBER,
            body='Hello from Twilio!'
        )
        print(rv)

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
        send_msg(user.profile.phone_number, event.end_datetime)
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
