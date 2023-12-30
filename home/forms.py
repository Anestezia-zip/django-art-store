from django import forms
from .models import PaintingRequest

class PaintingRequestForm(forms.ModelForm):
    class Meta:
        model = PaintingRequest
        exclude = ['user']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 10, 'style': 'height: 100px;'}),
        }
