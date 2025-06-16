from django.urls import path
from .views import register_organizer, register_attendee, CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/organizer/', register_organizer, name='register_organizer'),
    path('register/attendee/', register_attendee, name='register_attendee'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
