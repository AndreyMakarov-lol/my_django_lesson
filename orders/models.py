from django.db import models

# Create your models here.
class SalesOrder(models.Model):
    amount = models.IntegerField()
    description = models.CharField(max_length=250)
