from django.db import models
from django.core.validators import RegexValidator

phone_validator = RegexValidator(
    "^(0|\+[1-9]{2})[-., ]?[1-9]?([-., ]?[0-9]{2,}){4,}$"
    )


class Assignment(models.Model):
    employee = models.ForeignKey(
        'authentication.Employee', on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_revoked = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True


class TimeStamp(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class EmployeeClient(Assignment):
    client = models.ForeignKey(
        'events.Client', on_delete=models.CASCADE, null=True)


class EmployeeContract(Assignment):
    client = models.ForeignKey(
        'events.Contract', on_delete=models.CASCADE, null=True)


class EmployeeEvent(Assignment):
    client = models.ForeignKey(
        'events.Event', on_delete=models.CASCADE, null=True)


class Client(TimeStamp):
    active = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=True, blank=True)
    phone = models.CharField(
        max_length=16, validators=[phone_validator], null=True, blank=True)
    mobile = models.CharField(
        max_length=16, validators=[phone_validator], null=True, blank=True)
    company_name = models.CharField(max_length=100, null=True, blank=True)
    adress = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=80, null=True, blank=True)
    assignee = models.ManyToManyField(
        'authentication.Employee', through=EmployeeClient,
        related_name="clients")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Contract(TimeStamp):
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name="contracts")
    assignee = models.ManyToManyField(
        'authentication.Employee', through=EmployeeContract,
        related_name="contracts")
    signed = models.BooleanField(default=False)
    amount_in_euros = models.FloatField(default=0)
    payment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.client} ({self.date_created.date()})"


class Event(TimeStamp):
    name = models.CharField(max_length=100)
    contract = models.OneToOneField(
        Contract, null=True, blank=True, on_delete=models.CASCADE,
        related_name="event")
    assignee = models.ManyToManyField(
        'authentication.Employee', through=EmployeeEvent,
        related_name="events")

    def __str__(self):
        return f"{self.name}"
