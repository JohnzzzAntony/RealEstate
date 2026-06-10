from django.db import models

class Task(models.Model):
    class TaskType(models.TextChoices):
        RENEWAL = 'renewal', 'Renewal'
        EJARI = 'ejari', 'EJARI'
        INVOICE = 'invoice', 'Invoice'
        COMPLIANCE = 'compliance', 'Compliance'
        VACANCY = 'vacancy', 'Vacancy'
        DOCUMENT_EXPIRY = 'document_expiry', 'Document Expiry'
        FOLLOW_UP = 'follow_up', 'Follow-up'

    class Priority(models.TextChoices):
        LOW = 'low', 'Low'
        MEDIUM = 'medium', 'Medium'
        HIGH = 'high', 'High'
        URGENT = 'urgent', 'Urgent'

    class Status(models.TextChoices):
        OPEN = 'open', 'Open'
        IN_PROGRESS = 'in_progress', 'In Progress'
        COMPLETED = 'completed', 'Completed'
        OVERDUE = 'overdue', 'Overdue'
        CANCELLED = 'cancelled', 'Cancelled'

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    task_type = models.CharField(max_length=20, choices=TaskType.choices)
    priority = models.CharField(max_length=20, choices=Priority.choices, default=Priority.MEDIUM)
    due_date = models.DateField()

    # Generic relation link (optional, or just use specific FKs for common ones)
    linked_object_type = models.CharField(max_length=100, blank=True)
    linked_object_id = models.PositiveIntegerField(null=True, blank=True)

    assigned_to = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks')
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.OPEN)
    reminder_count = models.IntegerField(default=0)
    last_reminder_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.get_status_display()})"
