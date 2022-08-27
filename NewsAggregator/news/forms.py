from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Country, CountryFile, Category


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'country')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'country')


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ('name', 'code')


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = CountryFile
        fields = ('name', 'file')
