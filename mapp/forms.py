from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import item

class signupform(UserCreationForm):
    class Meta:
        model= User
        fields=['username','email','password1','password2']

class logform(forms.Form):
    username=forms.CharField(max_length=20)
    password=forms.CharField(max_length=20)


# class newitem(forms.ModelForm):
#     class Meta:
#         model = item
#         fields=['category','iname','des','price','image']
INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class newitem(forms.ModelForm):
    class Meta:
        model = item
        fields = ('category', 'iname', 'des', 'price', 'image',)
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'iname': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'des': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }
