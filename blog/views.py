from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, DetailView
from django.urls import reverse_lazy


class AddPost(CreateView):
    model = Post
    fields = ['title', 'content', 'image']
    template_name = 'blog/add_blog.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('blog_home')
    


class DisplayPost(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'

class DetailPost(DetailView):
    model = Post
    template_name = 'blog/detailed_post.html'




class UpdatePost(UpdateView):
    model = Post
    fields = ['title', 'content', 'image']
    template_name = 'blog/edit_blog.html'
    success_url = reverse_lazy('blog_home')


class DeletePost(DeleteView):
    model = Post
    template_name = 'blog/delete_blog.html'
    success_url = reverse_lazy('blog_home')
