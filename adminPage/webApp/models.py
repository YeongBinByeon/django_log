from django.db import models

# Create your models here.
class Utterance(models.Model):
    date = models.DateField()
    language = models.CharField(max_length=20) 
    mainAction = models.CharField(max_length=50) 
    utterance = models.CharField(max_length=100)

# Create your models here.
class Utterance1(models.Model):
    date = models.DateField()
    language = models.CharField(max_length=20) 
    mainAction = models.CharField(max_length=50) 
    utterance = models.CharField(max_length=100)

class KR_MainAction(models.Model):
    date = models.DateField()
    language = models.CharField(max_length=20)
    mainAction = models.CharField(max_length=50)
    count = models.PositiveIntegerField()
    rate = models.FloatField()