from django import forms
from .models import Signup, Login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class UserDetailsForm(forms.Form):
    name = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=10)
    place = forms.CharField(max_length=100)


class SignupForm(forms.ModelForm):
    class meta:
        model = Signup
        fields = "__all__"


class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ('email', 'password')
