from django.contrib import admin
from django.urls import reverse
from django.utils.html import escape, mark_safe
from django.contrib.auth import get_permission_codename
from .models import (
    Client,
    Contract,
    Event,
)


class AdminEvent(admin.ModelAdmin):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.extra_context = {}

    model = Event
    list_display = ['name', 'show_contract']

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
    search_fields = ['client']
    inlines = [InlineEvent]


class InlineContract(admin.StackedInline):
    model = Contract
    list_display = ['date_created', 'signed', 'payed']
    list_filter = ['signed', 'payed']
    search_fields = ['client']
    show_change_link = True
    extra = 0


class AdminClient(admin.ModelAdmin):
    model = Client
    list_display = ["first_name", "last_name", "phone", "mobile", "is_client"]
    search_fields = ["first_name", "last_name"]
    list_filter = ["active", "is_client"]
    inlines = [InlineContract]

    def has_add_permission(self, request):
        """
        Return True if the given request has permission to add an object.
        Can be overridden by the user in subclasses.
        """
        opts = self.opts
        codename = get_permission_codename("add", opts)
        return request.user.has_perm("%s.%s" % (opts.app_label, codename))

    def has_change_permission(self, request, obj=None):
        """
        Return True if the given request has permission to change the given
        Django model instance, the default implementation doesn't examine the
        `obj` parameter.
        Can be overridden by the user in subclasses. In such case it should
        return True if the given request has permission to change the `obj`
        model instance. If `obj` is None, this should return True if the given
        request has permission to change *any* object of the given type.
        """
        opts = self.opts
        codename = get_permission_codename("change", opts)
        return request.user.has_perm("%s.%s" % (opts.app_label, codename))

    def has_delete_permission(self, request, obj=None):
        """
        Return True if the given request has permission to change the given
        Django model instance, the default implementation doesn't examine the
        `obj` parameter.
        Can be overridden by the user in subclasses. In such case it should
        return True if the given request has permission to delete the `obj`
        model instance. If `obj` is None, this should return True if the given
        request has permission to delete *any* object of the given type.
        """
        opts = self.opts
        codename = get_permission_codename("delete", opts)
        return request.user.has_perm("%s.%s" % (opts.app_label, codename))

    def has_view_permission(self, request, obj=None):
        """
        Return True if the given request has permission to view the given
        Django model instance. The default implementation doesn't examine the
        `obj` parameter.
        If overridden by the user in subclasses, it should return True if the
        given request has permission to view the `obj` model instance. If `obj`
        is None, it should return True if the request has permission to view
        any object of the given type.
        """
        opts = self.opts
        codename_view = get_permission_codename("view", opts)
        codename_change = get_permission_codename("change", opts)
        return request.user.has_perm(
            "%s.%s" % (opts.app_label, codename_view)
        ) or request.user.has_perm("%s.%s" % (opts.app_label, codename_change))


admin.site.register(Client, AdminClient)
admin.site.register(Contract, AdminContract)
admin.site.register(Event, AdminEvent)
