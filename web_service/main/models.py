from django.db import models

# Create your models here.
class Message(models.Model):
    idd = models.CharField(null=False, max_length=100)
    message = models.CharField(null=False, max_length=1024)
    response = models.CharField(null=False, max_length=2000, default="HI")
