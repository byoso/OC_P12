from django.contrib import admin
from django.contrib.auth import get_permission_codename
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
