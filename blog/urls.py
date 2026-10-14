
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="blog_home"),
    path('add/', views.add_blog, name='add_blog'),
]
