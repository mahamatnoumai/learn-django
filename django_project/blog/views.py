from django.shortcuts import render
from . models import Post 
from django.views.generic import ListView, DetailView

# Create your views here.

def home(request):

    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(ListView):
    model = Post
    #template_name = 'blog/post_detail.html'

def about(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/about.html', context)

    