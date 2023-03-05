from django.contrib import admin
from .models import slogan, OrgDetails, register

# Register your models here.

admin.site.register(slogan)
admin.site.register(OrgDetails)
admin.site.register(register)