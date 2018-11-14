from django.db import models

# Create your models here.
class Post(models.Model):
	name = models.CharField(max_length=120)
	price = models.IntegerField()
	ISBN = models.CharField(max_length=120)
	def __str__(self):
		return self