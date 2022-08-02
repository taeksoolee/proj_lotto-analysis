from django.shortcuts import render, redirect

from blog.models import Post
from django.contrib.auth.models import User

def post_list(request):
  posts = Post.objects.all()

  return render(request, 'blog/post_list.html', {
    'title': 'hello world',
    'posts': posts,
  })

def create_post(request):
  if request.method == 'GET':
    return render(request, 'blog/create_post.html', {})
  
  elif request.method == 'POST':
    author = request.POST['author']
    title = request.POST['title']
    text = request.POST['text']

    me = User.objects.get(username='admin')
    Post.objects.create(author=me, title=title, text=text)

    return redirect('blog:post_list')
    