
from django.urls import path
from .views import HomePageFeed, UpdatePost, DeletePost, AddPost, DetailPost

urlpatterns = [
    path("", HomePageFeed.as_view(), name="blog_home"),
    path('detail/<int:pk>/', DetailPost.as_view(), name='detail_blog'),
    path('add/', AddPost.as_view(), name='add_blog'),
    path('edit/<int:pk>/', UpdatePost.as_view(), name = 'edit_blog'),
    path('delete/<int:pk>/', DeletePost.as_view(), name='delete_blog'),
]
