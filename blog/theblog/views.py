from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from .models import Post
from .forms import PostForm,EditForm

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

class UpdatePostView(UpdateView):
    model=Post
    form_class= EditForm
    template_name = "theblog/update_post.html"
