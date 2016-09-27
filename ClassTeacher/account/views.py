from django.shortcuts import render
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from account.forms import LoginForm
# Create your views here.


class LoginView(FormView):
    template_name = "account/login.html"
    form_class = LoginForm
    success_url = "/home"

    def form_valid(self, form):
        form_cleaned_data = form.cleaned_data
        username = form_cleaned_data.get('username')
        password = form_cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        return super(LoginView, self).form_invalid(form)


class RegisterView(CreateView):
    template_name = "account/signup.html"
    form_class = UserCreationForm
    success_url = "/account/signup-success"
