from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    username = forms.CharField(required=True,
                               min_length=4,
                               max_length=50,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'email'}))
    password = forms.CharField(required=True,
                               min_length=8, widget=forms.PasswordInput(
                                   attrs={'class': 'form-control', 'placeholder': 'contraseña'}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El nombre de usuario esta en uso')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El nombre de usuario esta en uso')
        return email
