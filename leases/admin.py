from django.contrib import admin
from .models import MainLease, Sublease

@admin.register(MainLease)
class MainLeaseAdmin(admin.ModelAdmin):
    list_display = ('lease_reference_number', 'property', 'lease_start_date', 'lease_end_date', 'status')
    list_filter = ('status',)

@admin.register(Sublease)
class SubleaseAdmin(admin.ModelAdmin):
    list_display = ('sublease_reference', 'subtenant', 'unit', 'lease_start_date', 'lease_end_date', 'status')
    list_filter = ('status',)
