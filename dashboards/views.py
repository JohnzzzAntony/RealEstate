from django.shortcuts import render
from properties.models import Property, PropertyUnit
from leases.models import Sublease
from audit_logs.models import AuditLog

def dashboard_view(request):
    context = {
        'properties_count': Property.objects.count(),
        'active_leases_count': Sublease.objects.filter(status='active').count(),
        'vacant_units_count': PropertyUnit.objects.filter(occupancy_status='vacant').count(),
        'recent_logs': AuditLog.objects.all().order_by('-created_at')[:10],
    }
    return render(request, 'dashboards/dashboard.html', context)
