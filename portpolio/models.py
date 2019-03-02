from django.db import models

# Create your models here.
class Portpolio(models.Model):
   title=models.CharField(max_length=100)
   image=models.ImageField(upload_to='images/')
   description=models.CharField(max_length=500)
   def __str__(self):
      return self.title