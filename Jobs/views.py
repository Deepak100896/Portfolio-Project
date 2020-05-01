from django.shortcuts import render
#import the model from the same directory and import job from it.
from .models import Job

# Create your views here.
def home(request):
    #the below line of code will bring all the jobs from the database using objects
    Jobs = Job.objects
    return render(request,'Jobs/home.html', {'Jobs':Jobs})
