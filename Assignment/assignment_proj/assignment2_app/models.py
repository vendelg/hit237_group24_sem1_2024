from django.db import models

# Create your models here.

class TestThesis(models.Model):   # Step 1
  title = models.CharField(max_length=100)
  desc = models.CharField(max_length=1500)
  sup_name = models.CharField(max_length=30)
  
  def __str__(self):
    return str(self.id) + " : " + self.title