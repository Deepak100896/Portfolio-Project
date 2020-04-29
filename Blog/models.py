from django.db import models

from datetime import datetime
# Below are the steps that we need to follow
# Crete Blog model
    # In blog model we will having title, pub_date,body,image
# Add the blog app to settings
# Create migrations
# Migrate
# Add to the admin

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = datetime.today().strftime('%Y-%m-%d')
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
