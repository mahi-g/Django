from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.posts, name = 'posts-posts'),
    #path('about/', views.about, name='posts-about')
]
