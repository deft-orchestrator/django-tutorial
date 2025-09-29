from django.shortcuts import render, get_object_or_404

from django.core.paginator import Paginator

def get_blog_posts(request):
    blog_posts = Post.objects.all().order_by('-published_date')
    paginator = Paginator(blog_posts, 5)  # 5 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blogs/post_list.html', {'page_obj': page_obj})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blogs/post_detail.html', {'post': post})