from django.db import models

# Create your models here.
class Patient(models.Model):
    pname=models.CharField(max_length=30)
    pno=models.IntegerField()
    pmarks=models.FloatField()
