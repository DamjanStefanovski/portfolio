from django.db import models

# Job descripting model representing past finished projects

class Job(models.Model):
    image = models.ImageField(upload_to='images/',blank=True,null=True)
    summary = models.CharField(max_length=200)
