import json

from django.shortcuts import render
from django.http import HttpResponse
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.formfields import PhoneNumberField
from accounts.models import *
from events.models import *

# Create your views here.

def sms(request):
    if request.method == "POST":
        from_number = str(request.body).split('&')[-2][8:]
        msg = str(request.body).split('&')[10][5:].split('+')

        confirm = msg[0]
        event_id = msg[1]

        twiml = ''
        if confirm.lower() == "yes":
            twiml = '<Response><Message>You successfully approved the request</Message></Response>'
            from_number='+'+from_number
            user = User.objects.get(profile__phone_number=from_number)
            event = Event.objects.get(id=event_id)
            event.pending.remove(user)
            event.verified.add(user)
            print(user)
        else:
            twiml = '<Response><Message>You successfully denied the request</Message></Response>'



        return HttpResponse(twiml, content_type='text/xml')
