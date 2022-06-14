from django.db import models
from django.contrib.auth.models import AbstractUser


class Employee(AbstractUser):

    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "Employee"

    @property
    def get_groups(self):
        return [group.name for group in self.groups.all()]
    # set a verbose name for django admin:
    get_groups.fget.short_description = 'groups'
