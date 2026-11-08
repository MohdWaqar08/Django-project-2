from .models import Post, Subreddits
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from . forms import PostForm, SubredditForm

# View to create posts
class AddPost(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_blog.html'
    success_url = reverse_lazy('blog_home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Handles subreddit creation
class CreateSubreddit(LoginRequiredMixin, CreateView):
    model = Subreddits
    form_class = SubredditForm
    template_name = 'blog/create_subreddit.html'
    success_url = reverse_lazy('blog_home') #later change to specific subreddit.

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
    
    


class HomePageFeed(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    paginate_by = 25

    def get_queryset(self):
        return Post.objects.select_related('subreddits', 'author').order_by('-created_on')

# Handles comments
class CommentView(DetailView):
    model = Post
    template_name = 'blog/comments.html'




class UpdatePost(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/Update_post_page.html'
    success_url = reverse_lazy('blog_home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DeletePost(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/delete_blog.html'
    success_url = reverse_lazy('blog_home')
