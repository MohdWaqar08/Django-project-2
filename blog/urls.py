
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="blog_home"),
    path('add/', views.add_blog, name='add_blog'),
    path('edit/<int:post_id>/', views.edit_blog, name = 'edit_blog'),
    path('delete/<int:post_id>/', views.delete_blog, name='delete_blog'),
]
