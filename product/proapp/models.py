from django.db import models

class prodb(models.Model):
    sl_no= models.IntegerField()
    proname= models.CharField(max_length=100)
    description= models.TextField()
    price=models.FloatField()
    discount=models.CharField(max_length=100)
