from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView ,DeleteView
from .models import Post,Category
from django.urls import reverse_lazy
from .forms import PostForm,EditForm

# Create your views here.

class HomeView(ListView):

    model = Post
    template_name="theblog/home.html"
    ordering=['post_date']

class ArticleDetailView(DetailView):
    model = Post
    template_name="theblog/detail.html"

class AddPostView(CreateView):
    model = Post
    template_name="theblog/add_post.html"
    form_class = PostForm
    
class AddCategoryView(CreateView):
    model = Category
    template_name="theblog/add_category.html"
    fields=['name']

class UpdatePostView(UpdateView):
    model=Post
    form_class= EditForm
    template_name = "theblog/update_post.html"

class DeletePostView(DeleteView):
    model = Post
    template_name = 'theblog/delete_post.html'
    success_url= reverse_lazy('home')
