from django import forms
from .models import User  # Import your User model

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'f_name', 'l_name', 'email', 'password']
        widgets = {'password': forms.PasswordInput()}
