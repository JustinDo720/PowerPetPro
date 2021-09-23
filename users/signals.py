from django.dispatch import receiver
from django.db.models.signals import post_save
from power_pet_pro_app.models import Profile, CustomUser


@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=CustomUser)
def save_profile(sender, instance, created, **kwargs):
    instance.profile.save()