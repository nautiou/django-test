from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Event, EventForm


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    return initiation(request)


def create_user(request):
    username = request.POST['username']
    password = request.POST['password']
    mail = request.POST['mail']

    user = User.objects.create_user(username, mail, password)
    user.save()
    return initiation(request)


def create_event(request):
    event = EventForm(request.POST)
    event.save()
    return evenements(request)


def remove_event(request, pk):
    if (request.user.has_perm("remove_event")):
        event = get_object_or_404(Event, pk=pk)
        event.delete()
    return evenements(request)


def logout_view(request):
    logout(request)
    return initiation(request)


def initiation(request):
    return render(request, 'initiation.html', {'active': 'initiation'})


def evenements(request):
    events = Event.objects.all
    return render(request, 'evenements.html', {'active': 'evenements', 'events': events, 'event_form': EventForm})


def cotisation(request):
    return render(request, 'cotisation.html', {'active': 'cotisation'})


def donateur(request):
    return render(request, 'donateur.html', {'active': 'donateur'})


def contact(request):
    return render(request, 'contact.html', {'active': 'contact'})


def torcy(request):
    return render(request, 'torcy.html', {'active': 'torcy'})
