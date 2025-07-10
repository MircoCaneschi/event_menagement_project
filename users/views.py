from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from .forms import CustomUserRegistrationForm
from django.urls import reverse_lazy

def register_organizer(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_organizer = True
            user.is_attendee = False
            user.save()
            login(request, user)
            return redirect('organizer_dashboard')
    else:
        form = CustomUserRegistrationForm()
    return render(request, 'users/register.html', {'form': form, 'role': 'organizer'})

def register_attendee(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_attendee = True
            user.is_organizer = False
            user.save()
            login(request, user)
            return redirect('/events/')
    else:
        form = CustomUserRegistrationForm()
    return render(request, 'users/register.html', {'form': form, 'role': 'Attendee'})


class CustomLoginView(LoginView):
    template_name = 'users/login.html'

    def get_success_url(self):
        user = self.request.user
        if user.is_organizer:
            return reverse_lazy('organizer_dashboard')
        elif user.is_attendee:
            return reverse_lazy('event_list')
        return reverse_lazy('login')
