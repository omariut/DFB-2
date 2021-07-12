from blog.models import Post
from django.shortcuts import render
from django.views.generic.edit import  UpdateView, DeleteView, CreateView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
# Create your views here.

class BlogListView(ListView):
    model=Post
    template_name='home.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = "new-post.html"
    fields = ['title', 'author', 'body']



class BlogDetailView(DetailView):
    model = Post
    template_name = "post-detail.html"

class BlogUpdateView(UpdateView):
    model = Post
    template_name = "post-edit.html"
    fields=['title', 'body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = "delete-post.html"
    success_url= reverse_lazy ('home')
