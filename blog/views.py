from django.shortcuts import render, redirect, get_object_or_404
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


@login_required
def edit_blog(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()
            return redirect('blog_home')
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/edit_blog.html', {
        'form': form,
        'post': post
    })

@login_required
def delete_blog(request, post_id):
    post = get_object_or_404(
        Post, id=post_id, author=request.user
    )

    if request.method == 'POST':
        post.delete()
        return redirect('blog_home')

    return render(request, 'blog/delete_blog.html', {
        'post': post
    })
