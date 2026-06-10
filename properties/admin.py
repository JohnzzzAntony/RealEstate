from django.contrib import admin
from .models import Property, PropertyUnit

class PropertyUnitInline(admin.TabularInline):
    model = PropertyUnit
    extra = 1

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('property_code', 'property_name', 'property_type', 'status')
    list_filter = ('property_type', 'status', 'ownership_type')
    inlines = [PropertyUnitInline]

@admin.register(PropertyUnit)
class PropertyUnitAdmin(admin.ModelAdmin):
    list_display = ('unit_code', 'unit_name', 'property', 'occupancy_status')
    list_filter = ('occupancy_status', 'unit_type')
