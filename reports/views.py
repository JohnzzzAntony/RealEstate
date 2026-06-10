from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from properties.models import Property, PropertyUnit
from leases.models import Sublease
from billing.models import Billing
from django.db.models import Sum, Count

@login_required
def report_list(request):
    return render(request, 'reports/report_list.html')

@login_required
def occupancy_report(request):
    total_units = PropertyUnit.objects.count()
    occupied_units = PropertyUnit.objects.filter(occupancy_status='occupied').count()
    occupancy_rate = (occupied_units / total_units * 100) if total_units > 0 else 0

    context = {
        'total_units': total_units,
        'occupied_units': occupied_units,
        'occupancy_rate': occupancy_rate,
        'units_by_type': PropertyUnit.objects.values('unit_type').annotate(count=Count('id'))
    }
    return render(request, 'reports/occupancy_report.html', context)

@login_required
def revenue_report(request):
    total_revenue = Billing.objects.filter(payment_status='paid').aggregate(Sum('total_amount'))['total_amount__sum'] or 0
    overdue_amount = Billing.objects.filter(payment_status='overdue').aggregate(Sum('total_amount'))['total_amount__sum'] or 0

    context = {
        'total_revenue': total_revenue,
        'overdue_amount': overdue_amount,
    }
    return render(request, 'reports/revenue_report.html', context)
