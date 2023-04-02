from django import forms

from .models import Item

INPUT_CLASSES = 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image')
    
        widgets = {
            'category': forms.Select(attrs={
                'placeholder': 'Enter product name',
                'class': INPUT_CLASSES,
            }),

            'name': forms.TextInput(attrs={
                'placeholder': 'Enter product name',
                'class': INPUT_CLASSES,
            }),

            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES,
            }),

            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),

            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES,
            }),
        }

# https://youtu.be/ZxMB6Njs3ck?t=5067

