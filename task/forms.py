from django import forms
from django.forms import widgets
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username','password','first_name','last_name','email']
#
#         widgets={
#             'username':forms.TextInput(attrs={'class':'form-control'}),
#             'password':forms.TextInput(attrs={'class':'form-control'}),
#             'first_name':forms.TextInput(attrs={'class':'form-control'}),
#             'last_name':forms.TextInput(attrs={'class':'form-control'}),
#             'email':forms.TextInput(attrs={'class':'form-control'})
#         }

class RegForm(UserCreationForm):

    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class SkillForm(forms.ModelForm):

    class Meta:
        model = Skill
        fields = ['Sname', 'percentage']