from django.db import models
from django.core.exceptions import ValidationError

class MainLease(models.Model):
    class RentFrequency(models.TextChoices):
        MONTHLY = 'monthly', 'Monthly'
        QUARTERLY = 'quarterly', 'Quarterly'
        SEMIANNUAL = 'semiannual', 'Semiannual'
        ANNUAL = 'annual', 'Annual'

    class Status(models.TextChoices):
        DRAFT = 'draft', 'Draft'
        PENDING = 'pending_approval', 'Pending Approval'
        ACTIVE = 'active', 'Active'
        EXPIRING = 'expiring', 'Expiring'
        EXPIRED = 'expired', 'Expired'
        RENEWED = 'renewed', 'Renewed'
        TERMINATED = 'terminated', 'Terminated'

    company = models.ForeignKey('companies.InternalTenantCompany', on_delete=models.CASCADE)
    property = models.ForeignKey('properties.Property', on_delete=models.CASCADE, related_name='main_leases')
    drec_landlord_name = models.CharField(max_length=255, default='DREC')
    drec_tenant_number = models.CharField(max_length=100)
    lease_reference_number = models.CharField(max_length=100, unique=True)
    lease_start_date = models.DateField()
    lease_end_date = models.DateField()
    rent_amount = models.DecimalField(max_digits=15, decimal_places=2)
    rent_frequency = models.CharField(max_length=20, choices=RentFrequency.choices)
    security_deposit_amount = models.DecimalField(max_digits=15, decimal_places=2)
    payment_terms = models.TextField(blank=True)
    renewal_notice_days = models.IntegerField(default=90)
    grace_period_days = models.IntegerField(default=0)
    ejari_required = models.BooleanField(default=True)
    ejari_number = models.CharField(max_length=100, blank=True)
    ejari_issue_date = models.DateField(null=True, blank=True)
    ejari_expiry_date = models.DateField(null=True, blank=True)
    signed_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)
    renewal_stage = models.CharField(max_length=100, blank=True)
    legal_notes = models.TextField(blank=True)
    finance_notes = models.TextField(blank=True)
    document_folder = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Main Lease {self.lease_reference_number} - {self.property.property_name}"

class Sublease(models.Model):
    class RenewalOption(models.TextChoices):
        AUTO = 'auto', 'Auto'
        MANUAL = 'manual', 'Manual'
        NONE = 'none', 'None'

    class Status(models.TextChoices):
        DRAFT = 'draft', 'Draft'
        ACTIVE = 'active', 'Active'
        EXPIRING = 'expiring', 'Expiring'
        EXPIRED = 'expired', 'Expired'
        TERMINATED = 'terminated', 'Terminated'
        VACATED = 'vacated', 'Vacated'

    company = models.ForeignKey('companies.InternalTenantCompany', on_delete=models.CASCADE)
    property = models.ForeignKey('properties.Property', on_delete=models.CASCADE)
    unit = models.ForeignKey('properties.PropertyUnit', on_delete=models.CASCADE)
    subtenant = models.ForeignKey('subtenants.Subtenant', on_delete=models.CASCADE)
    sublease_reference = models.CharField(max_length=100, unique=True)
    lease_start_date = models.DateField()
    lease_end_date = models.DateField()
    contract_signed_date = models.DateField(null=True, blank=True)
    rent_amount = models.DecimalField(max_digits=15, decimal_places=2)
    deposit_amount = models.DecimalField(max_digits=15, decimal_places=2)
    service_charge_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    vat_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=5.00)
    payment_frequency = models.CharField(max_length=50)
    payment_due_day = models.IntegerField(default=1)
    notice_days = models.IntegerField(default=60)
    grace_period_days = models.IntegerField(default=0)
    late_fee_policy = models.TextField(blank=True)
    renewal_option = models.CharField(max_length=20, choices=RenewalOption.choices, default=RenewalOption.MANUAL)
    ejari_required = models.BooleanField(default=True)
    ejari_number = models.CharField(max_length=100, blank=True)
    ejari_issue_date = models.DateField(null=True, blank=True)
    ejari_expiry_date = models.DateField(null=True, blank=True)
    move_in_date = models.DateField(null=True, blank=True)
    move_out_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)
    occupancy_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=100.00)
    approved_by = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True, blank=True, related_name='approved_subleases')
    approval_date = models.DateField(null=True, blank=True)
    remarks = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.lease_start_date and self.lease_end_date:
            if self.lease_start_date >= self.lease_end_date:
                raise ValidationError("Lease end date must be after start date.")

            # Check for overlapping leases for the same unit
            overlaps = Sublease.objects.filter(
                unit=self.unit,
                status='active',
                lease_start_date__lt=self.lease_end_date,
                lease_end_date__gt=self.lease_start_date
            )
            if self.pk:
                overlaps = overlaps.exclude(pk=self.pk)

            if overlaps.exists():
                raise ValidationError("This unit already has an active lease for the selected period.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Sublease {self.sublease_reference} - {self.subtenant.tenant_name}"
