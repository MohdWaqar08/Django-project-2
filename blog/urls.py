
from django.urls import path
from .views import (HomePageFeed, UpdatePost, DeletePost, 
                    AddPost, CommentView, CreateSubreddit, 
                    SubredditFeed, SearchFeed)

urlpatterns = [
    path("", HomePageFeed.as_view(), name="blog_home"),
    path('detail/<int:pk>/', CommentView.as_view(), name='comment'),
    path('add/', AddPost.as_view(), name='add_blog'),
    path('update/<int:pk>/', UpdatePost.as_view(), name = 'update_blog'),
    path('delete/<int:pk>/', DeletePost.as_view(), name='delete_blog'),
    path('create/', CreateSubreddit.as_view(), name = 'create_subreddit'),
    path('r/<slug:slug>/', SubredditFeed.as_view(), name = 'subreddit_feed'),
    path('search/', SearchFeed.as_view(), name= 'search_result'),
]
