from django.contrib import admin
from .models import Department
from .models import Role
from  .models import Employee
# Register your models here.

admin.site.register(Employee)

admin.site.register(Role)

admin.site.register(Department)