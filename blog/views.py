from .models import Post
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from . forms import PostForm


class AddPost(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_blog.html'
    success_url = reverse_lazy('blog_home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    


class HomePageFeed(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    paginate_by = 25

    def get_queryset(self):
        return Post.objects.select_related('subreddits', 'author').order_by('-created_on')

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
