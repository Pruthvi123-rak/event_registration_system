from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Registration

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

def register_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        Registration.objects.create(name=name, email=email, event=event)
        return redirect('event_list')

    return render(request, 'events/register.html', {'event': event})
