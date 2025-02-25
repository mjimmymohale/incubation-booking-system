from django.contrib.auth.models import AbstractUser
from django.db import models
class CustomUser(AbstractUser):
    business_name = models.CharField(max_length=255, blank=True, null=True)
    contact_number = models.CharField(max_length=15)
