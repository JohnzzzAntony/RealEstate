from django.db import models

class Property(models.Model):
    class PropertyType(models.TextChoices):
        WAREHOUSE = 'warehouse', 'Warehouse'
        PLOT = 'plot', 'Plot'
        OFFICE = 'office', 'Office'
        YARD = 'yard', 'Yard'
        SHOWROOM = 'showroom', 'Showroom'
        MIXED = 'mixed', 'Mixed'

    class OwnershipType(models.TextChoices):
        LEASED = 'leased', 'Leased'
        OWNED = 'owned', 'Owned'
        MANAGED = 'managed', 'Managed'

    class Status(models.TextChoices):
        ACTIVE = 'active', 'Active'
        EXPIRING = 'expiring', 'Expiring'
        EXPIRED = 'expired', 'Expired'
        VACANT = 'vacant', 'Vacant'
        UNDER_RENOVATION = 'under_renovation', 'Under Renovation'

    company = models.ForeignKey('companies.InternalTenantCompany', on_delete=models.CASCADE, related_name='properties')
    property_code = models.CharField(max_length=50, unique=True)
    property_name = models.CharField(max_length=255)
    plot_number = models.CharField(max_length=100, blank=True)
    zone = models.CharField(max_length=100, blank=True)
    emirate = models.CharField(max_length=100, default='Dubai')
    location_description = models.TextField(blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    property_type = models.CharField(max_length=20, choices=PropertyType.choices)
    ownership_type = models.CharField(max_length=20, choices=OwnershipType.choices)
    area_sqft = models.DecimalField(max_digits=15, decimal_places=2)
    area_sqm = models.DecimalField(max_digits=15, decimal_places=2)
    annual_main_rent = models.DecimalField(max_digits=15, decimal_places=2)
    rent_currency = models.CharField(max_length=10, default='AED')
    main_lease_start_date = models.DateField()
    main_lease_end_date = models.DateField()
    main_lease_notice_days = models.IntegerField(default=90)
    ejari_required = models.BooleanField(default=True)
    municipality_account_number = models.CharField(max_length=100, blank=True)
    dewa_account_number = models.CharField(max_length=100, blank=True)
    sewage_account_number = models.CharField(max_length=100, blank=True)
    water_account_number = models.CharField(max_length=100, blank=True)
    access_card_count = models.IntegerField(default=0)
    parking_count = models.IntegerField(default=0)
    loading_bays_count = models.IntegerField(default=0)
    power_capacity_kw = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    fire_certificate_required = models.BooleanField(default=True)
    fire_certificate_expiry_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.ACTIVE)
    remarks = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.property_name} ({self.property_code})"

    class Meta:
        verbose_name_plural = "Properties"

class PropertyUnit(models.Model):
    class UnitType(models.TextChoices):
        WAREHOUSE = 'warehouse', 'Warehouse'
        OFFICE = 'office', 'Office'
        YARD = 'yard', 'Yard'
        ROOM = 'room', 'Room'
        PLOT_SEGMENT = 'plot_segment', 'Plot Segment'
        MEZZANINE = 'mezzanine', 'Mezzanine'
        PARKING = 'parking', 'Parking'
        OTHER = 'other', 'Other'

    class OccupancyStatus(models.TextChoices):
        VACANT = 'vacant', 'Vacant'
        RESERVED = 'reserved', 'Reserved'
        OCCUPIED = 'occupied', 'Occupied'
        BLOCKED = 'blocked', 'Blocked'
        MAINTENANCE = 'maintenance', 'Maintenance'

    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='units')
    unit_code = models.CharField(max_length=50)
    unit_name = models.CharField(max_length=255)
    unit_type = models.CharField(max_length=20, choices=UnitType.choices)
    floor_level = models.CharField(max_length=50, blank=True)
    area_sqft = models.DecimalField(max_digits=15, decimal_places=2)
    area_sqm = models.DecimalField(max_digits=15, decimal_places=2)
    rentable_area_sqft = models.DecimalField(max_digits=15, decimal_places=2)
    occupancy_status = models.CharField(max_length=20, choices=OccupancyStatus.choices, default=OccupancyStatus.VACANT)
    utility_meter_reference = models.CharField(max_length=100, blank=True)
    fire_zone = models.CharField(max_length=100, blank=True)
    max_occupancy = models.IntegerField(null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.unit_name} - {self.property.property_name}"

    class Meta:
        unique_together = ('property', 'unit_code')
