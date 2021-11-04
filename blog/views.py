from django.db import models
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Post,Category
from taggit.models import Tag
# Create your views here.
from django.db.models import Count

class PostList(ListView):
    model = Post
    paginate_by = 8



class PostDetails(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tages"] = Tag.objects.all()
        context['categories'] = Category.objects.all().annotate(post_count= Count('Category_blog'))[:4][:5]
        context["recent_blog"] = Post.objects.all()[:3]
        return context
    