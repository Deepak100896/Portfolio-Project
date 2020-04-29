from django.contrib import admin

from .models import Job
# We need to register our job here so that whenever we make some changes we need to make migrations so that the latest changes will be present to load
# to the website
admin.site.register(Job)
