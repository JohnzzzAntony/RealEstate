from django.db import models

class Billing(models.Model):
    class LeaseType(models.TextChoices):
        MAIN_LEASE = 'main_lease', 'Main Lease'
        SUBLEASE = 'sublease', 'Sublease'

    class PaymentStatus(models.TextChoices):
        UNPAID = 'unpaid', 'Unpaid'
        PARTIAL = 'partial', 'Partial'
        PAID = 'paid', 'Paid'
        OVERDUE = 'overdue', 'Overdue'
        WAIVED = 'waived', 'Waived'

    class PaymentMethod(models.TextChoices):
        BANK_TRANSFER = 'bank_transfer', 'Bank Transfer'
        CASH = 'cash', 'Cash'
        CHEQUE = 'cheque', 'Cheque'
        CARD = 'card', 'Card'
        ONLINE = 'online', 'Online'

    company = models.ForeignKey('companies.InternalTenantCompany', on_delete=models.CASCADE)
    property = models.ForeignKey('properties.Property', on_delete=models.CASCADE)
    unit = models.ForeignKey('properties.PropertyUnit', on_delete=models.SET_NULL, null=True, blank=True)
    subtenant = models.ForeignKey('subtenants.Subtenant', on_delete=models.SET_NULL, null=True, blank=True)
    lease_type = models.CharField(max_length=20, choices=LeaseType.choices)
    invoice_number = models.CharField(max_length=100, unique=True)
    invoice_date = models.DateField()
    period_start = models.DateField()
    period_end = models.DateField()
    due_date = models.DateField()
    amount_before_vat = models.DecimalField(max_digits=15, decimal_places=2)
    vat_amount = models.DecimalField(max_digits=15, decimal_places=2)
    total_amount = models.DecimalField(max_digits=15, decimal_places=2)
    currency = models.CharField(max_length=10, default='AED')
    payment_status = models.CharField(max_length=20, choices=PaymentStatus.choices, default=PaymentStatus.UNPAID)
    payment_method = models.CharField(max_length=20, choices=PaymentMethod.choices, blank=True)
    receipt_number = models.CharField(max_length=100, blank=True)
    receipt_date = models.DateField(null=True, blank=True)
    outstanding_balance = models.DecimalField(max_digits=15, decimal_places=2)
    late_fee = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Invoice {self.invoice_number} - {self.total_amount} {self.currency}"

    class Meta:
        verbose_name_plural = "Billing Records"
