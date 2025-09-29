from django.contrib import admin
from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_name', 'email', 'photo', 'is_deleted')


admin.site.register(Employee, EmployeeAdmin)
