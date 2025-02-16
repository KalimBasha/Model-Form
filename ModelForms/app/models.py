from django.db import models
from django.core.validators import *
# Create your models here.

class Topic(models.Model):
    topic_name=models.CharField(max_length=50,primary_key=True)

class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic, on_delete=models.CASCADE)
    name=models.CharField(max_length=50,validators=[MaxLengthValidator(20)])
    url=models.URLField(max_length=200)
    email=models.EmailField(max_length=254,validators=[EmailValidator])

class AccessRecord(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    author=models.CharField(max_length=50)
    date=models.DateField(auto_now_add=False)