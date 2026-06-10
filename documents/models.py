from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Document(models.Model):
    class DocumentType(models.TextChoices):
        LEASE = 'lease', 'Lease Agreement'
        EJARI = 'ejari', 'Ejari Certificate'
        TRADE_LICENSE = 'trade_license', 'Trade License'
        ID_COPY = 'id_copy', 'ID Copy'
        PASSPORT_COPY = 'passport_copy', 'Passport Copy'
        INVOICE = 'invoice', 'Invoice'
        RECEIPT = 'receipt', 'Receipt'
        APPROVAL = 'approval', 'Approval'
        OTHER = 'other', 'Other'

    class Status(models.TextChoices):
        VALID = 'valid', 'Valid'
        EXPIRING = 'expiring', 'Expiring'
        EXPIRED = 'expired', 'Expired'
        ARCHIVED = 'archived', 'Archived'

    linked_object_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    linked_object_id = models.PositiveIntegerField()
    linked_object = GenericForeignKey('linked_object_type', 'linked_object_id')

    document_type = models.CharField(max_length=50, choices=DocumentType.choices)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/%Y/%m/%d/')
    version = models.CharField(max_length=20, default='1.0')
    expiry_date = models.DateField(null=True, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True)
    is_required = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.VALID)
    remarks = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.get_document_type_display()} - {self.title}"
