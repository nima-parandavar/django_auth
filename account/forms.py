from django.contrib.auth.models import User
from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm


# class RegisterForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']
#         widgets = {
#             'username': forms.TextInput(attrs={'class': 'form-control mb-3'}),
#             'email': forms.EmailInput(attrs={'class': 'form-control mb-3'}),
#             'password': forms.PasswordInput(attrs={'class': 'form-control mb-3'})
#         }


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'email': forms.EmailInput(attrs={'class': 'form-control mb-3'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control mb-3'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control mb-3'})
        }


class RegisterProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        widgets = {
            'photo': forms.FileInput(attrs={'class': 'form-control mb-3'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control mb-3', 'type': 'date'}),
            'bio': forms.Textarea(attrs={'class': 'form-control mb-3'})
        }


class LoginForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control mb-3'}))