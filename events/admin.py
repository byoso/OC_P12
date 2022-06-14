from django.shortcuts import get_object_or_404
from django.contrib import admin
from django.urls import reverse
from django.utils.html import escape, mark_safe
from django.contrib.auth import get_permission_codename, get_user_model
from django.contrib.auth.models import Group
from .models import (
    Client,
    EmployeeClient,
    Contract,
    EmployeeContract,
    Event,
    EmployeeEvent,
)

Employee = get_user_model()


class InlineClientAssignment(admin.TabularInline):
    model = EmployeeClient
    list_display = ['username']
    extra = 1


class InlineContractAssignment(admin.TabularInline):
    model = EmployeeContract
    list_display = ['username']
    extra = 1


class InlineEventAssignment(admin.TabularInline):
    model = EmployeeEvent
    list_display = ['username']
    extra = 1


class AdminEvent(admin.ModelAdmin):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.extra_context = {}

    model = Event
    list_display = ['name', 'id', 'show_contract']
    inlines = [InlineEventAssignment]

    def _get_link(self, obj):
        link_string = reverse(
            "admin:events_contract_change", args=[obj.contract.id])
        link = mark_safe(f'<a href="{link_string}">{str(obj.contract)}</a>')
        self.extra_context['link'] = link
        return link

    def show_contract(self, obj):
        link = self._get_link(obj)
        return link


class InlineEvent(admin.StackedInline):
    model = Event
    show_change_link = True
    extra = 0


class AdminContract(admin.ModelAdmin):
    model = Contract
    list_display = ['client', 'id', 'date_created', 'signed', 'payed']
    list_filter = ['signed', 'payed']
    search_fields = [
        'client__last_name', 'client__company_name',
        'date_created']
    inlines = [InlineContractAssignment, InlineEvent]


class InlineContract(admin.StackedInline):
    model = Contract
    list_display = ['date_created', 'signed', 'payed']
    list_filter = ['signed', 'payed']
    search_fields = ['client']
    show_change_link = True
    extra = 0


class AdminClient(admin.ModelAdmin):
    model = Client
    list_display = [
        "first_name", "last_name", "id", "phone", "mobile",
        "is_client", "active"]
    search_fields = ["first_name", "last_name"]
    list_filter = ["active", "is_client"]
    inlines = [InlineClientAssignment, InlineContract]


admin.site.register(Client, AdminClient)
admin.site.register(Contract, AdminContract)
admin.site.register(Event, AdminEvent)
