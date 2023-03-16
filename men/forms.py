from django import forms
from .models import *
from django.core.exceptions import ValidationError

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

