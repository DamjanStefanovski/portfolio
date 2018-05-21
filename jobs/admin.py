from django.contrib import admin

# Register your models here.

from .models import Job

admin.site.register(Job)  # This Admin side to be improved for quicker and more efficant editing of the posts, from mobile or any other enviorment.  
