from django.contrib import admin
from .models import Manager,Employee

# Register your models here.


class ManagerDetail(admin.ModelAdmin):
    list_display = ['name', 'age', 'department', 'created_date', 'modified_date']
    list_filter = ['age']


class EmployeeDetails(admin.ModelAdmin):
    list_display = ['name', 'age', 'created_date', 'modified_date', 'reporting_manager']
    list_filter = ['salary']
    search_fields = ['name']
    fieldsets = (
        ("Section 1", {
                'fields': ('name', 'age')
            }),
        ("Section 2", {
            'fields': ('salary', 'designation')
        }),
        ("Section 3", {
            'fields': ['reporting_manager']
        }),
    )


admin.site.register(Manager, ManagerDetail)
admin.site.register(Employee, EmployeeDetails)
