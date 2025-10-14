from django.shortcuts import render, get_object_or_404
from .models import BlogPost

def blog_list(request):
    """List all published blog posts"""
    blogs = BlogPost.objects.filter(is_published=True).order_by('-published_at')
    return render(request, 'blog/list.html', {'blogs': blogs})

def blog_detail(request, slug):
    """Blog post detail view"""
    blog = get_object_or_404(BlogPost, slug=slug, is_published=True)
    return render(request, 'blog/detail.html', {'blog': blog})
