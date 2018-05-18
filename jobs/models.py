from django.db import models
# Job descripting model representing past finished projects

class Job(models.Model):
    image = models.ImageField(upload_to='images/',blank=True,null=True)
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=600)


    def __unicode__(self):  #this is a function/method and publish is the name of the method
        self.title
        self.save()
#indent methods inside the class
    def __str__(self):
        return self.title
