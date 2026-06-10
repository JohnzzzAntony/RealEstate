from django.db import models

class InternalTenantCompany(models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'active', 'Active'
        INACTIVE = 'inactive', 'Inactive'
        ARCHIVED = 'archived', 'Archived'

    company_code = models.CharField(max_length=50, unique=True)
    legal_name = models.CharField(max_length=255)
    trade_name = models.CharField(max_length=255, blank=True)
    tenant_number_drec = models.CharField(max_length=100, blank=True)
    emirate = models.CharField(max_length=100, default='Dubai')
    country = models.CharField(max_length=100, default='UAE')
    license_number = models.CharField(max_length=100, blank=True)
    license_issue_date = models.DateField(null=True, blank=True)
    license_expiry_date = models.DateField(null=True, blank=True)
    rera_registration_number = models.CharField(max_length=100, blank=True)
    vat_registered = models.BooleanField(default=False)
    vat_number = models.CharField(max_length=100, blank=True)
    trn_number = models.CharField(max_length=100, blank=True)
    office_address = models.TextField(blank=True)
    po_box = models.CharField(max_length=50, blank=True)
    contact_person_name = models.CharField(max_length=255, blank=True)
    contact_person_phone = models.CharField(max_length=50, blank=True)
    contact_person_email = models.EmailField(blank=True)
    company_owner_name = models.CharField(max_length=255, blank=True)
    company_owner_phone = models.CharField(max_length=50, blank=True)
    company_owner_email = models.EmailField(blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.ACTIVE)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.legal_name

    class Meta:
        verbose_name_plural = "Internal Tenant Companies"
