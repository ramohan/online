from django.db import models
class login(models.Model):
	username=models.CharField(max_length=20)
	password=models.CharField(max_length=20)
class signup(models.Model):
	login_name=models.CharField(max_length=20)
	fullname=models.CharField(max_length=20)
	password=models.CharField(max_length=20)
	phone_num=models.IntegerField()	
	

# Create your models here.
