from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post


@login_required
def add_blog(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog_home')
    else:
        form = PostForm()

    return render(request, 'blog/add_blog.html', {
        'form': form
    })


def home(request):
    posts = Post.objects.select_related('author').order_by('-created_at')

    return render(request, 'blog/home.html', {
        'posts': posts
    })
