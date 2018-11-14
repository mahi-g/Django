from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
#from django.urls import reverse

# Create your models here.
class Products(models.Model):
	book_name = models.CharField(max_length = 120)
	price = models.IntegerField()
	ISBN = models.CharField(max_length=120)
	author = models.CharField(max_length = 120)

	date_posted = models.DateTimeField(default=timezone.now)

	course = models.TextField(max_length=120)
	dept_id = models.TextField(max_length=120)

	seller = models.ForeignKey(User, on_delete=models.CASCADE)

	buyer = models.CharField(max_length=50, blank=True)


	def __str__(self):
		return self.book_name

	#def get_absolute_url(self):
    #    return reverse('post-detail', kwargs={'pk': self.pk})

