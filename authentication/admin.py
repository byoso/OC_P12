from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Employee


class EmployeeAdmin(UserAdmin):
    pass


admin.site.register(Employee, EmployeeAdmin)
