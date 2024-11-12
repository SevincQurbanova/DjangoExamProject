# from django.contrib import admin
# from .models import Department, Position, Employee
from django.contrib import admin
from django.utils.translation import gettext as _  # Make sure this line is included
from .models import Department, Position, Employee

class DepartmentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Department._meta.fields if field.name != 'id']  # Display all fields except 'id' in the list view
    fields = [field.name for field in Department._meta.fields if field.name not in ['id', 'created_at', 'updated_at']]  # Exclude 'id', 'created_at', 'updated_at' in the detail view

admin.site.register(Department, DepartmentAdmin)

class PositionAdmin(admin.ModelAdmin):
    # Display translated name
    list_display = ['translated_name', 'salary', 'department']
    
    def translated_name(self, obj):
        """
        This method uses Django's gettext function to dynamically translate the 'name' field.
        Make sure translations are defined for each string in your .po files.
        """
        return _(obj.name)  # Translate the name field dynamically based on the active language
    translated_name.short_description = 'Name'  # This sets the column name in the admin list view

    # Optionally specify fields to show in the detail view, excluding specific ones
    fields = [field.name for field in Position._meta.fields if field.name not in ['id', 'created_at', 'updated_at']]

admin.site.register(Position, PositionAdmin)


# class PositionAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in Position._meta.fields if field.name != 'id']  # Display all fields except 'id' in the list view
#     fields = [field.name for field in Position._meta.fields if field.name not in ['id', 'created_at', 'updated_at']]  # Exclude 'id', 'created_at', 'updated_at' in the detail view

# admin.site.register(Position, PositionAdmin)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Employee._meta.fields if field.name != 'id']  # Display all fields except 'id' in the list view
    fields = [field.name for field in Employee._meta.fields if field.name not in ['id', 'created_at', 'updated_at']]  # Exclude 'id', 'created_at', 'updated_at' in the detail view

admin.site.register(Employee, EmployeeAdmin)
