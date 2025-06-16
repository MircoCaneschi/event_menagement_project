from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    is_organizer = models.BooleanField(default=False)
    is_attendee = models.BooleanField(default=True)  # it's attendee by default

    def __str__(self):
        return self.username

# Create your models here.