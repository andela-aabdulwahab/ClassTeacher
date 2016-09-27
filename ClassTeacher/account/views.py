from django.shortcuts import render
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth.forms import UserCreationForm
from account.forms import LoginForm
# Create your views here.


class LoginView(FormView):
    template_name = "account/login.html"
    form_class = LoginForm
    success_url = "/home"

    def form_valid(self, form):
        pass


class RegisterView(CreateView):
    template_name = "account/signup.html"
    form_class = UserCreationForm
    success_url = "/account/signup-success"
