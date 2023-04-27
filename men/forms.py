from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm
from captcha.fields import CaptchaField

class AddProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Men
        fields = ['title','slug','content','photo','is_published','cat','content1','content2']

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'cols':30, 'rows':5,'class':'form-control'}),
            'content1': forms.Textarea(attrs={'cols': 30, 'rows': 5,'class':'form-control'}),
            'content2': forms.Textarea(attrs={'cols': 30, 'rows': 5,'class':'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),

        }


        def clean_title(self):
            title = self.cleaned_data['title']
            if len(title) > 200:
                raise ValidationError('Длина превышает 200 символов')

            return title


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class':'form-input'})),
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class':'form-input'})),
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-input'})),
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-input'})),
    class Meta:
        model = User
        fields = ('username',  'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Login", widget=forms.TextInput(attrs={'class':'form-input'})),
    password = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-input'}))


class ContactForm(forms.Form):
    name = forms.CharField(label='name',max_length=255)
    email = forms.EmailField(label='Email')
    content = forms.CharField(widget = forms.Textarea(attrs={'cols':60,'rows':10}))
    captcha = CaptchaField()