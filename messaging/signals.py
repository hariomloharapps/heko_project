# signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Message, Notification

@receiver(post_save, sender=Message)
def create_notification(sender, instance, created, **kwargs):
    if created:
        # Create a notification for the recipient user
        Notification.objects.create(user=instance.receiver, content="You have a new message.")