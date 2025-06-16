from django.urls import path
from . import views
from .views import (
    organizer_dashboard,
    EventCreateView,
    EventUpdateView,
    EventDeleteView
)

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('dashboard/', organizer_dashboard, name='organizer_dashboard'),
    path('create/', EventCreateView.as_view(), name='event_create'),
    path('<int:pk>/edit/', EventUpdateView.as_view(), name='event_edit'),
    path('<int:pk>/delete/', EventDeleteView.as_view(), name='event_delete'),
    path('<int:pk>/join/', views.register_to_event, name='event_register'),
    path('my-events/', views.my_events, name='my_events'),
    path('<int:pk>/leave/', views.unregister_from_event, name='event_unregister'),



]