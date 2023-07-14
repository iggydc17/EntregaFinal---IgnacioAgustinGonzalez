from django import forms
from .models import Mensaje


class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['contenido']
        widgets = {
            'contenido': forms.TextInput(attrs={
                'class': 'message-input',
                'style': 'width: 90%; padding: 8px; border: none; border-radius: 5px; outline: none;'
            })
        }
