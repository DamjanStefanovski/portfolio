from django.db import models
from django.utils import timezone

# Class

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    url =  models.URLField(max_length=500, blank=True)

    def __str__(self):
        return self.title


    def summary(self):
        return self.body[:625]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')













# Add to settings. > Create a migration. > migrate. > add to the admin view
# Templates, > Staticfiles, Forms. and urls.py . acordingly
