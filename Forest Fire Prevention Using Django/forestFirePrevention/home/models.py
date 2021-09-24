from django.db import models

# Create your models here.
class Fire(models.Model):
    oxygen = models.IntegerField()
    temperature = models.IntegerField()
    humidity = models.IntegerField()
    output = models.FloatField()