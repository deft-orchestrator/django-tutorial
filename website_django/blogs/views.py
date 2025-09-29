
from django.shortcuts import render
from .models import Post

def post_list(request):
	blog_posts = Post.objects.all()
	return render(request, 'blogs/post_list.html', {'blog_posts': blog_posts})
