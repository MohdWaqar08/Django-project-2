from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class Subreddits(models.Model):
    name = models.CharField(max_length=50, unique = True)
    slug = models.SlugField(max_length=50, unique = True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_subreddits')

    def __str__(self):
        return f"r/{self.name}"

    
class Post(models.Model):
    subreddits = models.ForeignKey(Subreddits, on_delete=models.CASCADE, related_name='posts')
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name="posts")
    title = models.CharField(max_length=500)
    content = models.TextField()
    url = models.URLField(blank = True, null = True)
    image = models.ImageField(
        #save to blog/images
        upload_to = 'blog/images/',
        blank = True,
        null = True,
    )
    created_on = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title

class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return f"Comment by {self.author} on {self.post}"