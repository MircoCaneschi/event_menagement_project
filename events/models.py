from django.db import models
from django.conf import settings

class Event(models.Model):
    title= models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    organizer= models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='organized_events'
    )

    def __str__(self):
        return f"{self.title} ({self.date})"

class Registration(models.Model):
    attendee=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='registrations'
    )
    event=models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='registrations'
    )
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"(self.attendee.username)-> {self.event.title}"



# Create your models here.
