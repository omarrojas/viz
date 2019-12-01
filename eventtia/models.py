from django.db import models

# Create your models here.
class tp3edgelist(models.Model):
    source=models.IntegerField();
    target=models.TextField();
    weight=models.IntegerField();
    year = models.IntegerField();
    month = models.TextField();
    type=models.TextField();
    
class ts31eventtype(models.Model):
    type=models.TextField();
    year = models.IntegerField();
    month = models.TextField();
    