from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sms(request):
    if request.method == "POST":
        print(request)
        twiml = '<Response><Message>Hello from your Django app!</Message></Response>'
        return HttpResponse(twiml, content_type='text/xml')
