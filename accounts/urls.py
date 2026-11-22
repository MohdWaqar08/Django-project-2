
from django.urls import path,reverse_lazy
from django.contrib.auth.views import (LoginView, LogoutView, 
                                       PasswordChangeView, PasswordChangeDoneView)
from . views import RegisterView 


urlpatterns = [
   path("register/", RegisterView.as_view(), name="register"),
   path("login/", LoginView.as_view(template_name = 'accounts/login.html'), name="login"),
   path("logout/", LogoutView.as_view(next_page = 'login'), name="logout"),
   path('password-change/', 
        PasswordChangeView.as_view(template_name = 'accounts/password_change.html',
                                   success_url = reverse_lazy('password-change-done')   ), 
                                   name= 'password_change'),
   path('password-change/done', 
        PasswordChangeDoneView.as_view(template_name = 'accounts/password_change_done.html'
                                       ), name= 'password-change-done'),                 
]
