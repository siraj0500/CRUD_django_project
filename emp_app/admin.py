from django.contrib import admin
from .models import Employee_reg


class EmpAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'contact_number', 'email', 'pic')


# Register your models here.
admin.site.register(Employee_reg, EmpAdmin)
