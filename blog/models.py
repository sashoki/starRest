# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.base_user import AbstractBaseUser
import uuid
from django.utils.safestring import mark_safe
from django.utils import timezone





# Create your models here.

class UserProfile(models.Model):
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User Profile')
    logo = models.ImageField(null=True, blank=True, upload_to="logo/", verbose_name='Logo', help_text="50x50")
    full_name = models.CharField(max_length=25, verbose_name='Full name')
    uniq_identifi = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,
                                     verbose_name='Unique identificator')  # primary_key = True,

    def __str__(self):
        return f'{self.full_name or self.uniq_identifi}'

    def __unicode__(self):
        return f'{self.full_name or self.uniq_identifi}'

    def sender_email(obj):
        return f'{obj.user.email}'
    sender_email.short_description = 'E-mail'

    def sender_user(obj):
        return f'{obj.user.username}'
    sender_user.short_description = 'Name'

    def bit_logo(self):
        if self.logo:
            return mark_safe('<img src="%s" style="width: 30px; height:30px;" />' % self.logo.url)
        else:
            return 'Logo not selected'
    bit_logo.short_description = 'Logo'
    bit_logo.allow_tags = True


class Post(models.Model):
    class Meta():
        ordering = ['-post_date']
        db_table = 'post'
        verbose_name_plural = 'Post'
        verbose_name = 'Posts'

    post_title = models.CharField(max_length=200, verbose_name=u'Title')
    post_text = models.TextField(null=True, blank=True, verbose_name=u'Text')
    post_date = models.DateTimeField(default=timezone.now, verbose_name=u'Create data')
    post_author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u'Post autor')


    def __str__(self):
        return self.post_title

