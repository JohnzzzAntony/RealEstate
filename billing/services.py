from datetime import date
from .models import Billing
from leases.models import Sublease

def generate_invoices_for_lease(sublease):
    """
    Simple service to generate the next invoice for a sublease.
    In a production app, this would be more complex (handling schedules).
    """
    # Check if invoice for this month already exists
    today = date.today()
    if not Billing.objects.filter(
        sublease=sublease,
        period_start__year=today.year,
        period_start__month=today.month
    ).exists():
        vat_amount = sublease.rent_amount * (sublease.vat_percentage / 100)
        total = sublease.rent_amount + vat_amount

        Billing.objects.create(
            company=sublease.company,
            property=sublease.property,
            unit=sublease.unit,
            subtenant=sublease.subtenant,
            lease_type='sublease',
            invoice_number=f"INV-{sublease.sublease_reference}-{today.strftime('%Y%m')}",
            invoice_date=today,
            period_start=today.replace(day=1),
            period_end=today, # placeholder
            due_date=today, # placeholder
            amount_before_vat=sublease.rent_amount,
            vat_amount=vat_amount,
            total_amount=total,
            outstanding_balance=total,
            payment_status='unpaid'
        )
