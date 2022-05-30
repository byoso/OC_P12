from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Employee


class EmployeeAdmin(UserAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name', 'is_active']


admin.site.register(Employee, EmployeeAdmin)
