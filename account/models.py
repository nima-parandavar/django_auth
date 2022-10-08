from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    photo = models.ImageField(blank=True)
    phone_number = models.CharField(max_length=11, blank=True)
    birth_date = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user}"


# signals
@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
    user = kwargs.get('instance')
    created = kwargs.get('created')

    if created:
        profile = Profile(user=user)
        profile.save()