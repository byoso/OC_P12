from django.contrib import admin
from .models import (
    Client,
    Contract,
    Event,
)


class AdminClient(admin.ModelAdmin):
    model = Client
    list_display = ["first_name", "last_name", "phone", "mobile", "active"]
    search_fields = ["first_name", "last_name"]
    list_filter = ["active"]


class AdminContract(admin.ModelAdmin):
    model = Contract
    list_display = ['client', 'date_created', 'signed']
    list_filter = ['signed']
    search_fields = ['client']


class AdminEvent(admin.ModelAdmin):
    model = Event


admin.site.register(Client, AdminClient)
admin.site.register(Contract, AdminContract)
admin.site.register(Event, AdminEvent)
