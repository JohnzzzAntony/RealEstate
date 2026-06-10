from django.db import models

class Subtenant(models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'active', 'Active'
        EXPIRING = 'expiring', 'Expiring'
        VACANT = 'vacant', 'Vacant'
        TERMINATED = 'terminated', 'Terminated'
        BLACKLISTED = 'blacklisted', 'Blacklisted'

    class RiskLevel(models.TextChoices):
        LOW = 'low', 'Low'
        MEDIUM = 'medium', 'Medium'
        HIGH = 'high', 'High'

    company = models.ForeignKey('companies.InternalTenantCompany', on_delete=models.CASCADE)
    property = models.ForeignKey('properties.Property', on_delete=models.CASCADE)
    unit = models.ForeignKey('properties.PropertyUnit', on_delete=models.SET_NULL, null=True, blank=True)
    subtenant_code = models.CharField(max_length=50, unique=True)
    tenant_name = models.CharField(max_length=255)
    legal_entity_name = models.CharField(max_length=255)
    trade_license_number = models.CharField(max_length=100, blank=True)
    trade_license_expiry_date = models.DateField(null=True, blank=True)
    passport_number = models.CharField(max_length=100, blank=True)
    emirates_id = models.CharField(max_length=100, blank=True)
    nationality = models.CharField(max_length=100, blank=True)
    contact_person = models.CharField(max_length=255, blank=True)
    contact_phone = models.CharField(max_length=50, blank=True)
    contact_email = models.EmailField(blank=True)
    billing_email = models.EmailField(blank=True)
    vat_number = models.CharField(max_length=100, blank=True)
    trn_number = models.CharField(max_length=100, blank=True)
    business_activity = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.ACTIVE)
    risk_level = models.CharField(max_length=20, choices=RiskLevel.choices, default=RiskLevel.LOW)
    remarks = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tenant_name
