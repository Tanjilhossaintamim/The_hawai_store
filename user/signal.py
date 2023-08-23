from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings

from store.models import Customer


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_customer_profile_whenever_user_create(sender, instance, created, **Kwargs):
    if created:
        Customer.objects.create(user=instance)
