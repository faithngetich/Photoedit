from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class FacebookUser(User):
  pass
  
class Image(models.Model):
  category = models.Foreignkey(Category),
  date_created = models.DateField(auto_now_add=True),
  date_modified = models.DateField(auto_now=True),
  uploader = models.CharField(max_length=200),
  image_name = models.CharField(max_length=200)

class Category(models.Models):
  name = models.CharField(max_length=200)