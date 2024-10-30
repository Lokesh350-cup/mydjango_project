 #forms_app/forms.py
from django import forms

class ForName(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control','placeholder': 'Enter your name'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-contorl', 'placeholder': 'Enter your email'
        })
    )
    feedback = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control', 'placeholder': 'Enter your feedback'
        })
    )

    profile_pic = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control-file'
        })


    )