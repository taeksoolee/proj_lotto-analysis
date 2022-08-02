from django.urls import path
from . import views

app_name = 'blog' # set namespace

urlpatterns = [
  path('', views.post_list, name='post_list'),
  path('create_post', views.create_post, name='create_post')
]