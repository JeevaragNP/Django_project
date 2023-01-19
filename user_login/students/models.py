from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=50)
    roll_no = models.IntegerField()
    marks = models.FloatField(max_length=50)
    image_url = models.CharField(max_length=2556)
