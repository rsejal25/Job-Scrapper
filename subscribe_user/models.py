from django.db import models

# Create your models here.
class Subscribed_Users(models.Model):
 #username=models.CharField(max_length=30)
 email=models.CharField(max_length=50)
 designation=models.CharField(max_length=100)
 location=models.CharField(max_length=80)
 user_id=models.IntegerField()

