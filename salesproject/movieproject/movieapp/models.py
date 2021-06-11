from django.db import models

# Create your models here.
class MovieForm(models.Model):
    mname=models.CharField(max_length=30)
    heroname=models.CharField(max_length=30)
    heroinname=models.CharField(max_length=30)
    directorname=models.CharField(max_length=30)
    rating=models.IntegerField()
