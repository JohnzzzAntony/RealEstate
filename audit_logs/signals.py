from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from django.db import connection
from .models import AuditLog

@receiver(post_save)
def log_save(sender, instance, created, **kwargs):
    if sender == AuditLog:
        return
    # Avoid errors if table doesn't exist (e.g. during tests/migrations)
    if 'audit_logs_auditlog' not in connection.introspection.table_names():
        return

    action = 'Created' if created else 'Updated'
    try:
        AuditLog.objects.create(
            action=action,
            entity_type=sender.__name__,
            entity_id=str(instance.pk),
            after_data={'status': getattr(instance, 'status', 'N/A')}
        )
    except:
        pass
