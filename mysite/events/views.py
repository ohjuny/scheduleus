from django.shortcuts import render

# Create your views here.
def create(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():

            return render(request, "event.html")
        else:
            return render(request, "create.html", {
                'form': form,
            })
    else:
        form = UserForm()
        return render(request, "create.html", {
            'form': form,
        })



    return render(request, "create.html")