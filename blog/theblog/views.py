from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from django.urls import reverse_lazy, reverse
from .forms import PostForm, EditForm
from django.http import HttpResponseRedirect

# Create your views here.


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))


class HomeView(ListView):

    model = Post
    template_name = "theblog/home.html"
    ordering = ['post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


def CategoryView(request, cat):
    # cat=cat.replace('-',' ')
    catlist = Post.objects.filter(category=cat)
    return render(request, 'theblog/categories.html', {'cat': cat.title(), 'catlist': catlist})


def CategoryListView(request):
    # cat=cat.replace('-',' ')
    catlistmenu = Category.objects.all()

    return render(request, 'theblog/category_list.html', {'catlistmenu': catlistmenu})


class ArticleDetailView(DetailView):
    model = Post
    template_name = "theblog/detail.html"

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        post_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context = super(ArticleDetailView, self).get_context_data(
            *args, **kwargs)
        context["cat_menu"] = cat_menu
        context["total_likes"] = post_likes
        context["liked"] = liked
        return context


class AddPostView(CreateView):
    model = Post
    template_name = "theblog/add_post.html"
    form_class = PostForm

    # def get_context_data(self, *args , **kwargs):
    #     cat_menu = Category.objects.all()
    #     context= super(AddPostView,self).get_context_data(*args , **kwargs)
    #     context["cat_menu"]=cat_menu
    #     return context


class AddCategoryView(CreateView):
    model = Category
    template_name = "theblog/add_category.html"
    fields = ['name']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddCategoryView, self).get_context_data(
            *args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "theblog/update_post.html"

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(UpdatePostView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class DeletePostView(DeleteView):
    model = Post
    template_name = 'theblog/delete_post.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(DeletePostView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
