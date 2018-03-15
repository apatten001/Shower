from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .forms import RegisterForm

# Create your views here.


class HomeView(TemplateView):
    template_name = 'home.html'


class RegisterFormView(CreateView):

    form_class = RegisterForm
    template_name = 'guest_register.html'


