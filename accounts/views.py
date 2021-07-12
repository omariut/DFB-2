from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls.base import reverse_lazy
from django.views.generic import CreateView

# Create your views here.
class SignUpView(CreateView):
    model=User
    template_name='registration/signup.html'
    success_url=reverse_lazy('login')
    fields=['username', 'password']