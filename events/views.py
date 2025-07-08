from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Registration
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import EventForm
from django.contrib import messages


def event_list(request):
    events = Event.objects.all().annotate(registration_count=Count('registrations')).order_by('date')
    joined_event_ids = []

    if request.user.is_authenticated and (request.user.is_attendee or request.user.is_organizer):
        joined_event_ids = Registration.objects.filter(attendee=request.user).values_list('event_id', flat=True)

    return render(request, 'events/event_list.html', {
        'events': events,
        'joined_event_ids': joined_event_ids
    })


@login_required
def organizer_dashboard(request):
    if not request.user.is_organizer:
        if settings.DEBUG:
            return render(request, '403.html', status=403)
        else:
            raise PermissionDenied

    events = Event.objects.filter(organizer=request.user) \
        .annotate(registration_count=Count('registrations')) \
        .order_by('date')
    return render(request, 'events/organizer_dashboard.html', {'events': events})


# CRUD views for Event model
class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_form.html'

    def form_valid(self, form):
        form.instance.organizer = self.request.user
        messages.success(self.request, "Event created successfully.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('organizer_dashboard')


class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_form.html'

    def get_queryset(self):
        messages.success(self.request, "Event updated successfully.")
        return Event.objects.filter(organizer=self.request.user)

    def get_success_url(self):
        return reverse_lazy('organizer_dashboard')


class EventDeleteView(DeleteView):
    model = Event
    template_name = 'events/event_confirm_delete.html'

    def get_queryset(self):
        return Event.objects.filter(organizer=self.request.user)

    def get_success_url(self):
        return reverse_lazy('organizer_dashboard')


@login_required
def register_to_event(request, pk):
    if not (request.user.is_attendee or request.user.is_organizer):
        return HttpResponseForbidden("Only authenticated users can register.")

    event = get_object_or_404(Event, pk=pk)
    already_registered = Registration.objects.filter(event=event, attendee=request.user).exists()

    if already_registered:
        messages.warning(request, "You are already registered for this event.")
    else:
        Registration.objects.create(event=event, attendee=request.user)
        messages.success(request, "You have successfully registered.")

    return redirect('event_list')


@login_required
def my_events(request):
    if not request.user.is_attendee and not request.user.is_organizer:
        return HttpResponseForbidden("Only attendees can view their events.")

    registrations = Registration.objects.filter(attendee=request.user).select_related('event')
    return render(request, 'events/my_events.html', {'registrations': registrations})


@login_required
def unregister_from_event(request, pk):
    if not (request.user.is_attendee or request.user.is_organizer):
        return HttpResponseForbidden("Only authenticated users can unregister.")

    registration = Registration.objects.filter(event_id=pk, attendee=request.user).first()
    if registration:
        registration.delete()
        messages.success(request, "You have successfully unregistered.")
    else:
        messages.warning(request, "You were not registered for this event.")

    return redirect('event_list')

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')