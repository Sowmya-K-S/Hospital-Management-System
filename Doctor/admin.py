from django.contrib import admin
from Doctor.models import  Doctor_table,DepartmentTable


# Register your models here.
admin.site.register(Doctor_table)
admin.site.register(DepartmentTable)