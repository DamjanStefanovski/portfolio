from django.db import models
from django.utils import timezone

# Class

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    

    def __str__(self):
        return self.title






# Add to settings. > Create a migration. > migrate. > add to the admin view
# Templates, > Staticfiles, Forms. and urls.py . acordingly
