from django.shortcuts import render
from apps.post.models import Post, Tag
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class PostIndex(LoginRequiredMixin, TemplateView):
    login_url = 'user-login'
    redirect_field_name = 'next'

    def get(self, request):

        index = Post.objects.all()
        # tags = Post.objects.values('tags').annotate(name=Tag.name)

        context = {
            'index': index,
            # 'tags': tags,
        }

        return render(
            request,
            template_name="post/post_index.html",
            context=context
        )


class Homepage(TemplateView):
    def get(self, request):

        return render(
            request,
            template_name="post/homepage.html",

        )


class About(TemplateView):
    def get(self, request):

        return render(
            request,
            template_name="post/about.html",
        )
