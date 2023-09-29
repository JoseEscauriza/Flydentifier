from django.urls import reverse_lazy
from django import forms
from apps.post.forms import PostForm
from django.shortcuts import render, redirect
from apps.post.models import Post
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class PostIndex(LoginRequiredMixin, TemplateView):
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


class NewPost(LoginRequiredMixin, CreateView):
    template_name = "post/newpost.html"
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('post-index')

    def form_valid(self, form):
        handler = self.request.user
        form.instance.user_id = handler
        return super().form_valid(form)
