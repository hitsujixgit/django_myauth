# -*- Coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.decorators import login_required

@login_required
def page(request):
    if request.POST:
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            username       = request.POST['username']
            password       = request.POST['password']
            email          = request.POST['email']
            new_user = User.objects.create_user(username = username, email = email, password=password)
            new_user.is_active = True
            new_user.save()
            return render(request, 'jp/add_user_successful.html')
    
    else:
        form = MyUserCreationForm()
    return render(request, 'jp/add_user.html', {'form' : form})

class MyUserCreationForm(forms.Form):
    username = forms.CharField(label = "User name")
    password = forms.CharField(label = "Password", widget = forms.PasswordInput)
    password_bis = forms.CharField(label = "Password", widget = forms.PasswordInput) 
    email = forms.EmailField(label = "Email")
    def clean(self):
        cleaned_data = super(MyUserCreationForm, self).clean() 
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password') 
        password_bis = self.cleaned_data.get('password_bis')
        if password and password_bis and password != password_bis:
            raise forms.ValidationError("Passwords are not identical.")
        user_check = User.objects.filter(username = username)
        try:
            user_check.get()
        except Exception:
            # when no exists duplicate username
            return self.cleaned_data
        raise forms.ValidationError("Duplicate user name!")
