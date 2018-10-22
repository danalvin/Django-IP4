from django import forms
from .models import *


class NewProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']


class NewNeigbor_hood_Form(forms.ModelForm):
    class Meta:
        model = nieghbor
        fields = ['name', 'location']


class New_Business_Form(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user']


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user']


class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['user', 'date_posted', 'post']
