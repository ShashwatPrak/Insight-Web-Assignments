from django.forms import *
from .models import Articles


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = '__all__'
        widgets = {
            'title': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 500px;',
                'placeholder': 'Enter Article Title'
            }),
            'author': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 500px;',
                'placeholder': 'Author of Article'
            }),
            'publish_date': NumberInput(attrs={'type': 'date', 'class': "form-control"}),
            'category': Select(attrs={
                'class': "form-control",
                'style': 'max-width: 500px;',
                'placeholder': 'Select Category'
            }),
        }
