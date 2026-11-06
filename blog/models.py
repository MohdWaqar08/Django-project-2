from django.conf import settings
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    title = models.CharField(max_length=500)
    content = models.TextField()
    image = models.ImageField(
        #save to blog/images
        upload_to = 'blog/images/',
        blank = True,
        null = True,
    )
    created_on = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title
