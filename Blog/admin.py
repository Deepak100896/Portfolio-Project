from django.contrib import admin

# Register your models here.
from .models import Blog
# We need to register our job here so that whenever we make some changes we need to make migrations so that the latest changes will be present to load
# to the website
#Once you have register the app you will be able to see this job in admin
admin.site.register(Blog)
