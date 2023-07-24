# signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Notification


@receiver(post_save, sender=User)
def create_teacher_notification(sender, instance, created, **kwargs):
    if created:
        if instance.groups.filter(name="Teacher").exists():
            # Create a new notification for the admin
            message = f"A new teacher account ({instance.username}) has been created."
            Notification.objects.create(message=message)
