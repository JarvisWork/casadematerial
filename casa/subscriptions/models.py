from django.db import models

class Subscription(models.Model):
	name = models.CharField(max_length=100)
	cpf = models.CharField(max_length=11, unique=True)
	name_shop = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	district = models.CharField(max_length=100)
	city = models.CharField(max_length=100)
	UF = models.CharField(max_length=2)
	email = models.EmailField(unique=True)
	phone = models.CharField(max_length=20,blank=True)
	create_at = models.DateTimeField(auto_now_add=True)

# Create your models here.
