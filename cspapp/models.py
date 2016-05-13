from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from	django.core.urlresolvers	import	reverse
from django.db.models.signals import post_save
# Create your models here.
from django.dispatch import receiver
from django.conf import settings
from annoying.fields import AutoOneToOneField
from datetime import date


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
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="media", blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    department = models.ForeignKey(Department, default=1)
    developers = models.ForeignKey(All_users, blank=True, null=True)

    def __unicode__(self):
        return u"%s" % self.id

    def get_absolute_url(self):
        return reverse('cspapp:projects_detail', kwargs={'pk': self.pk})


class Comment (models.Model):
    author = models.TextField()
    body = models.TextField()
    project = models.IntegerField(Project)

    def __unicode__(self):
        return u"%s" % self.id

    def get_absolute_url(self):
        return reverse('cspapp:comment_project', kwargs={'pk': self.pk})


class Review(models.Model):
    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    rating = models.PositiveSmallIntegerField('Rating (stars)', blank=False, default=3, choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)


class ProjectReview(Review):
    project = models.ForeignKey(Project)


class Activity(models.Model):
    title = models.TextField()
    description = models.TextField(blank=True, null=True)
    statement = models.TextField()
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)

    def __unicode__(self):
        return u"%s" % self.id

    def get_absolute_url(self):
        return reverse('cspapp:activities_detail', kwargs={'pk': self.pk})


class ProjectActivity(Activity):
    project = models.ForeignKey(Project)
    creator = models.ForeignKey(User, default=1)


class Answer(models.Model):
    body = models.TextField()
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)


class ActivityAnswer(Answer):
    project = models.ForeignKey(Activity)
    creator = models.ForeignKey(User, default=1)
