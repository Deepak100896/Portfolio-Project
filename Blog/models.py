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
    pub_date = models.DateTimeField(default=datetime.now, blank=True)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

#We can create function inside a class which will have self as a parameter and use it to modify the
# values that we are getting from the database using the models

#Fxn which will rename the object1, object2 that we are seeing in the admin page with the title of the blog
    def __str__(self):
        return self.title

#Function which will return the first 100 letters from the body
    def summary(self):
        return self.body[:100]

#Function which will return only date from the pub_date
    def onlydate(self):
        return self.pub_date.strftime('%Y-%m-%d')
