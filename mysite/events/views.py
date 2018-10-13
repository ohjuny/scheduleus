from django.shortcuts import render
from .forms import *

# Create your views here.
def create(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        print('HELLO HELLO HELLO')
        print(form)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            print('ASDFGHJKJL')
            event = form.save()
            return render(request, "home.html")
        else:
            print('QWERTY')
            return render(request, "create.html", {
                'form': form,
            })
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