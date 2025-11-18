from django.contrib import admin

# Register your models here.
from .models import Ushtari

class AdminDisplay(admin.ModelAdmin):
    list_display = [
        "name", 'father_name', 'family_name', 'pob', 'personal_id'
    ]


# Executef
admin.site.register(Ushtari, AdminDisplay)