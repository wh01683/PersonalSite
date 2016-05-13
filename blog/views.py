from django.shortcuts import render


# Create your views here.
from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import *
# Create your views here.


def index(request):
    post_list = Post.objects.order_by('-pub_date')
    context = {
        'post_list': post_list
    }
    return render(request, 'blog/index.html', context)


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comment_list = get_list_or_404(Comment, post=post)
    context = {
        'post': post,
        'comment_list': comment_list
    }
    return render(request, 'blog/detail.html', context)
