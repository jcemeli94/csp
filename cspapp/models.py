from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
from django.dispatch import receiver
from django.conf import settings


class Project(models.Model):
    id_proj = models.IntegerField(unique=True, primary_key=True)


class All_users(models.Model):
    user = models.OneToOneField(User)
    category = models.TextField(null=True)

    def __str__(self):
          return "%s's profile" % self.user

# Create an UserProfile when an user is created.
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile_for_new_user(sender, created, instance, **kwargs):
    if created:
        profile = All_users(user=instance)
        profile.save()
