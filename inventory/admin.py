from django.contrib import admin
from .models import SparePart

class SparePartAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'quantity')
    search_fields = ['name', 'description']

admin.site.register(SparePart, SparePartAdmin)
