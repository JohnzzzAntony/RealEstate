from django.test import TestCase
from django.core.exceptions import ValidationError
from datetime import date, timedelta
from companies.models import InternalTenantCompany
from properties.models import Property, PropertyUnit
from subtenants.models import Subtenant
from leases.models import Sublease

class LeaseOverlapTest(TestCase):
    def setUp(self):
        self.company = InternalTenantCompany.objects.create(
            company_code='C1', legal_name='Test Company'
        )
        self.property = Property.objects.create(
            company=self.company, property_code='P1', property_name='P1',
            property_type='warehouse', ownership_type='owned',
            area_sqft=1000, area_sqm=100, annual_main_rent=10000,
            main_lease_start_date=date(2023, 1, 1), main_lease_end_date=date(2025, 1, 1)
        )
        self.unit = PropertyUnit.objects.create(
            property=self.property, unit_code='U1', unit_name='U1',
            unit_type='warehouse', area_sqft=1000, area_sqm=100, rentable_area_sqft=1000
        )
        self.subtenant = Subtenant.objects.create(
            company=self.company, property=self.property, unit=self.unit,
            subtenant_code='S1', tenant_name='Sub1', legal_entity_name='Sub1'
        )

    def test_overlapping_lease_fails(self):
        # Create first active lease
        Sublease.objects.create(
            company=self.company, property=self.property, unit=self.unit,
            subtenant=self.subtenant, sublease_reference='L1',
            lease_start_date=date(2024, 1, 1), lease_end_date=date(2024, 12, 31),
            rent_amount=1000, deposit_amount=100, payment_frequency='Annual',
            status='active'
        )

        # Try to create an overlapping active lease
        overlapping_lease = Sublease(
            company=self.company, property=self.property, unit=self.unit,
            subtenant=self.subtenant, sublease_reference='L2',
            lease_start_date=date(2024, 6, 1), lease_end_date=date(2025, 6, 1),
            rent_amount=1000, deposit_amount=100, payment_frequency='Annual',
            status='active'
        )

        with self.assertRaises(ValidationError):
            overlapping_lease.full_clean()
