# -*- coding: utf-8 -*-

from django.contrib import admin
from blog.models import UserProfile, Post
from django_reverse_admin import ReverseModelAdmin                                                      # pip install django_reverse_admin
# from django.contrib.admin.models import LogEntry
from blog.forms import UserForm


class UserProfileAdmin(ReverseModelAdmin):
    inline_reverse = [('user', {'form': UserForm, 'exclude':('password')})]                              # show User on place UserProfile
    inline_type = 'stacked'                                                                              # or could be 'tabular'
    fields = ['logo', 'full_name']
    list_display = ('bit_logo', 'full_name', 'uniq_identifi')

class PostAdmin(admin.ModelAdmin):
    fields = ['post_title', 'post_text',  'post_date', 'post_author']
    list_display = ('post_title', 'post_text',  'post_date', 'post_author')
    search_fields = ['blog_title', 'post_author']


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Post, PostAdmin)
