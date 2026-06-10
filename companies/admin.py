from django.contrib import admin
from .models import InternalTenantCompany

@admin.register(InternalTenantCompany)
class InternalTenantCompanyAdmin(admin.ModelAdmin):
    list_display = ('company_code', 'legal_name', 'status', 'created_at')
    search_fields = ('company_code', 'legal_name')
    list_filter = ('status', 'emirate')
