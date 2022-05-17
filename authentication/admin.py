from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Employee


class EmployeeAdmin(UserAdmin):
    list_display = ['username', 'first_name', 'last_name', 'is_active']


admin.site.register(Employee, EmployeeAdmin)
