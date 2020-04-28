from django.db import models

# Create your models here.
# Model object will be saved in the database with the below line of code
class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    #ImageField inherits from FileField according to Django documentation
    summary = models.CharField(max_length =200)
