from django.db import models

class EjariRegistration(models.Model):
    class ApprovalStatus(models.TextChoices):
        NOT_STARTED = 'not_started', 'Not Started'
        SUBMITTED = 'submitted', 'Submitted'
        APPROVED = 'approved', 'Approved'
        REJECTED = 'rejected', 'Rejected'
        CANCELLED = 'cancelled', 'Cancelled'

    sublease = models.ForeignKey('leases.Sublease', on_delete=models.CASCADE, related_name='ejari_registrations')
    ejari_number = models.CharField(max_length=100, blank=True)
    application_number = models.CharField(max_length=100, blank=True)
    issue_date = models.DateField(null=True, blank=True)
    expiry_date = models.DateField(null=True, blank=True)
    registered_by = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True, blank=True)
    submitted_date = models.DateField(null=True, blank=True)
    approval_status = models.CharField(max_length=20, choices=ApprovalStatus.choices, default=ApprovalStatus.NOT_STARTED)
    rejection_reason = models.TextField(blank=True)
    attached_document = models.FileField(upload_to='ejari_docs/', blank=True, null=True)
    renewal_required = models.BooleanField(default=False)
    reminders_sent = models.IntegerField(default=0)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Ejari {self.ejari_number} for Sublease {self.sublease.sublease_reference}"
