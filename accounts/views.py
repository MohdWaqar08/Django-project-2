from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy('login')
