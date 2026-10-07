from django.contrib import admin
from .models import Property


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ("title", "location", "city", "price", "property_type", "status", "is_featured")
    list_filter = ("property_type", "status", "is_featured", "city")
    search_fields = ("title", "location", "city")
    list_editable = ("is_featured", "status")