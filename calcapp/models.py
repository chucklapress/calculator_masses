from django.db import models

# Create your models here.

class SavedCalc(models.Model):
    left = models.IntegerField()
    operators = models.CharField(max_length=15)
    right = models.IntegerField()
    total = models.FloatField()
    loguser = models.CharField(max_length=25)

class SaveUser(models.Model):
    saveuser = models.ForeignKey(SavedCalc)
