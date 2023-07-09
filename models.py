from django.db import models


# Create your models here.


class Login_USER(models.Model):
 username=models.CharField(max_length=30)
 email=models.CharField(max_length=30) 
 address=models.CharField(max_length=30)
 password=models.CharField(max_length=30)
 

 