from django.db import models
from django.utils import timezone
# Job descripting model representing past finished projects

class Job(models.Model):
    image = models.ImageField(upload_to='images/',blank=True,null=True)
    title = models.CharField(max_length=200)
    summary = models.TextField(max_length=1000)
    url =  models.URLField(max_length=500, blank=True)
    pub_date = models.DateTimeField()


    def __unicode__(self):  #this is a function/method and publish is the name of the method
        self.title
        self.save()
#indent methods inside the class
    def __str__(self):
        return self.title

    
