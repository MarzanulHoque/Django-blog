from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from .models import Post
from .forms import PostForm

# Create your views here.

class HomeView(ListView):

    model = Post
    template_name="theblog/home.html"

class ArticleDetailView(DetailView):
    model = Post
    template_name="theblog/detail.html"

class AddPostView(CreateView):
    model = Post
    template_name="theblog/add_post.html"
    form_class = PostForm
