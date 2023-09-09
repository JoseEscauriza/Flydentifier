from django.shortcuts import render
from apps.post.models import Post

# Create your views here.


def post_index(request):
    index = Post.objects.all()

    context = {
        'index': index
    }

    return render(
        request,
        template_name="post/post_index.html",
        context=context
    )


def homepage(request):

    return render(
        request,
        template_name="post/homepage.html"
    )
