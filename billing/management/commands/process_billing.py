from django.core.management.base import BaseCommand
from django.utils import timezone
from billing.models import Billing
from leases.models import Sublease
from billing.services import generate_invoices_for_lease

class Command(BaseCommand):
    help = 'Processes billing: generates new invoices and marks overdue'

    def handle(self, *args, **options):
        today = timezone.now().date()

        # 1. Mark overdue
        overdue_bills = Billing.objects.filter(due_date__lt=today, payment_status='unpaid')
        count = overdue_bills.count()
        for bill in overdue_bills:
            bill.payment_status = 'overdue'
            bill.save()

        # 2. Generate new invoices for active subleases
        active_subleases = Sublease.objects.filter(status='active')
        for lease in active_subleases:
            generate_invoices_for_lease(lease)

        self.stdout.write(self.style.SUCCESS(f'Successfully processed billing. Marked {count} overdue.'))
