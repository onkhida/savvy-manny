from django.shortcuts import render
from .models import Post

def post_list(request):
    my_posts = Post.objects.all()

    context = {
        'posts':my_posts
    }

    return render(request, "blog/post_list.html", context)