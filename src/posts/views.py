from django.shortcuts import render
from django.http import HttpResponse

#from django.contrib.auth import authenticate, get_user_model, login, logout

from .models import Post

# Create your views here.
def posts(request):
	all_posts = Post.objects.all() #grab all objects from Post tables
	context = {
		'all_posts':all_posts
	}
	return render(request, "posts/posts_list.html", context)
