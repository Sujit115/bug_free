from django.db import models
from datetime import datetime
# Create your models here.

class Realtor(models.Model):
  
  name = models.CharField(max_length=200, default = "")
  photo = models.ImageField(upload_to='photos/%Y/%m/%d/', default = "")
  description = models.TextField(blank=True, default = "")
  phone = models.CharField(max_length=20, default = "")
  email = models.CharField(max_length=50, default = "")
  is_mvp = models.BooleanField(default=False)
  hire_date = models.DateTimeField(default=datetime.now, blank=True)

  def __str__(self):
    return self.name