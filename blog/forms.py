# -*- encoding: UTF-8 -*-
from django import forms
from .models import user


class LoginForm(forms.Form):
    email = forms.CharField(label='email', max_length=100)
    password = forms.CharField(label='password', max_length=100)
    # remember_me = forms.CheckboxInput()


class LoginModel(user):

    def __init__(self, request):
        self.email = request.POST['email']
        self.password = request.POST['password']

    def is_valid(self):
        return True
        # pass


