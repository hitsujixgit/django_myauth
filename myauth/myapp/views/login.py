# -*- Coding: utf-8 -*-
from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth import authenticate, login

def page(request):
    
    if request.POST:
        form = Login_form(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if request.GET.get('next') is not None:
                        # Redirect to a success page.
                        return redirect(request.GET['next'])
    
    # New form when not the request is get.
    else:
        form = Login_form()
    return render(request, 'jp/login.html', {'form' : form})

class Login_form(forms.Form):
    username = forms.CharField(label="User name")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    def clean(self):
        cleaned_data = super(Login_form, self).clean()
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if not authenticate(username=username, password=password):
            raise forms.ValidationError("Wrong user name or passwsord")
        return self.cleaned_data