from django.shortcuts import render
from .models import Job

# This are basic views that can be improved with bringing more into the Models.py filie and increesing volume of the project itself.
def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})
