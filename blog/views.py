from django.shortcuts import get_object_or_404, redirect
from .models import Post, Subreddits
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, DetailView
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from . forms import PostForm, SubredditForm, CommentForm

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
class CommentView(FormMixin,DetailView):
    model = Post
    form_class = CommentForm
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_success_url(self):
        return reverse('comment', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all().order_by('created_at')
        if 'form' not in context:
            context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)
        else: 
            return self.form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit = False)
        comment.post = self.object
        comment.author = self.request.user
        comment.save()
        return redirect(self.get_success_url())




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
