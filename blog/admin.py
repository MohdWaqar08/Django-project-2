from django.contrib import admin
from .models import Post, Subreddits, Comments, Vote
# Register your models here.
admin.site.register(Post)
admin.site.register(Subreddits)
admin.site.register(Comments)
admin.site.register(Vote)