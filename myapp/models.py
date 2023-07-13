from django.db import models

class jsondata(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    detail = models.CharField(max_length=10)
    data = models.JSONField()
    date = models.DateTimeField()
    def __str__(self):
        return str(self.latitude)+","+str(self.longitude)
    
# Create your models here.
