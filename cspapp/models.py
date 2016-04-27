from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from	django.core.urlresolvers	import	reverse
from django.db.models.signals import post_save
# Create your models here.
from django.dispatch import receiver
from django.conf import settings
from annoying.fields import AutoOneToOneField


# Create your models here.
class All_users(models.Model):
    user = AutoOneToOneField(User, primary_key=True)
    category = models.TextField(null=True)

    def __str__(self):
          return "%s's profile" % self.user

    # Create an UserProfile when an user is created.
# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_profile_for_new_user(sender, created, instance, **kwargs):
#     if created:
#         profile = All_users(user=instance)
#         profile.save()


class Department(models.Model):
    name = models.TextField(blank=True, null=True)
    cap_dep = models.ForeignKey(All_users, blank=True, null=True)

    def __unicode__(self):
        return u"%s" % self.id


class Project(models.Model):
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="media", blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    department = models.ForeignKey(Department, default=1)
    developers = models.ForeignKey(All_users, blank=True, null=True)

    def __unicode__(self):
        return u"%s" % self.id

    def get_absolute_url(self):
        return reverse('cspapp:projects_detail', kwargs={'pk': self.pk})


