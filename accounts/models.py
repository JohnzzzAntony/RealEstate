from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Roles(models.TextChoices):
        SUPER_ADMIN = 'SUPER_ADMIN', 'Super Admin'
        LEGAL_COMPLIANCE = 'LEGAL_COMPLIANCE', 'Legal / Compliance Manager'
        PROPERTY_MANAGER = 'PROPERTY_MANAGER', 'Property Manager'
        LEASE_ADMIN = 'LEASE_ADMIN', 'Lease Administrator'
        FINANCE_OFFICER = 'FINANCE_OFFICER', 'Finance Officer'
        READ_ONLY = 'READ_ONLY', 'Read-only Management User'

    role = models.CharField(
        max_length=20,
        choices=Roles.choices,
        default=Roles.READ_ONLY
    )
    phone_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
