from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    fullName = models.CharField(max_length=64, blank=False, null=False)
    email = models.EmailField(max_length=64, blank=False, null=False)
    phoneNumber = models.CharField(max_length=64, blank=False, null=False)
    def __str__(self):
        return self.username