
from django.urls import path
from . import views
from .views import DisplayPost, UpdatePost, DeletePost, AddPost

urlpatterns = [
    path("", DisplayPost.as_view(), name="blog_home"),
    path('add/', AddPost.as_view(), name='add_blog'),
    path('edit/<int:pk>/', UpdatePost.as_view(), name = 'edit_blog'),
    path('delete/<int:pk>/', DeletePost.as_view(), name='delete_blog'),
]
