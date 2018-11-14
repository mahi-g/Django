from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Products

@login_required
def home(request):
	context = {
	    'posts' : Products.objects.all()
	 }
	return render(request, 'shop/home.html', context)