from django.contrib import admin
from .models import Household

# Register your models here.
@admin.register(Household)
class PersonAdmin(admin.ModelAdmin):
    list_filter = ['studenthousehold__primary']
