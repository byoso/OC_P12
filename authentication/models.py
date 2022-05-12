from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class Employee(AbstractUser):

    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
