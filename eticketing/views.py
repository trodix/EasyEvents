from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.views import generic
from .models import Event

def list_events(request):
    events = Event.objects.all()
    return render(request, 'eticketing/event.html', {
        'event_list': events
    })


def event_detail(request, id):
    event = Event.objects.get(pk=id)
    return render(request, 'eticketing/event_detail.html', {
        'event': event
    })


@csrf_protect
def event_order(request, id):
    event = Event.objects.get(pk=id)

    if request.method == 'POST':
        print(request)
        return render(request, 'eticketing/event_order.html', {
            'event': event,
            'message': 'Votre réservation a été enregistrée'
        })

    return render(request, 'eticketing/event_order.html', {
        'event': event
    })
