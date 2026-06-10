from django.core.management.base import BaseCommand
from django.utils import timezone
from leases.models import MainLease, Sublease
from tasks_notifications.models import Task

class Command(BaseCommand):
    help = 'Checks for leases approaching expiry and creates tasks'

    def handle(self, *args, **options):
        today = timezone.now().date()
        threshold = today + timezone.timedelta(days=90)

        # Check Main Leases
        expiring_main = MainLease.objects.filter(lease_end_date__lte=threshold, status='active')
        for lease in expiring_main:
            Task.objects.get_or_create(
                title=f"Renewal for Main Lease {lease.lease_reference_number}",
                task_type='renewal',
                due_date=lease.lease_end_date,
                status='open',
                defaults={'description': f"Lease for {lease.property.property_name} expires on {lease.lease_end_date}"}
            )
            lease.status = 'expiring'
            lease.save()

        # Check Subleases
        expiring_sub = Sublease.objects.filter(lease_end_date__lte=threshold, status='active')
        for lease in expiring_sub:
            Task.objects.get_or_create(
                title=f"Renewal for Sublease {lease.sublease_reference}",
                task_type='renewal',
                due_date=lease.lease_end_date,
                status='open',
                defaults={'description': f"Sublease for {lease.subtenant.tenant_name} expires on {lease.lease_end_date}"}
            )
            lease.status = 'expiring'
            lease.save()

        self.stdout.write(self.style.SUCCESS('Successfully checked lease expiries'))
