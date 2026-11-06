from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import UserRegistrationForm
from django.contrib.auth.models import User


class RegisterView(CreateView):
    model = User
    from_class = UserRegistrationForm
    fields = ('username', 'email')
    template_name = "accounts/register.html"
    success_url = reverse_lazy('login')
