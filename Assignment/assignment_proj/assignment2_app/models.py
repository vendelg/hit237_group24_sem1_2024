from django.db import models

# Create your models here.

class Project(models.Model):
  TID = models.CharField(max_length=3, primary_key=True)
  title = models.CharField(max_length=100)
  desc = models.CharField(max_length=1500)
  supName = models.CharField(max_length=30)
  
  def __str__(self):
    return self.TID + " : " + self.title