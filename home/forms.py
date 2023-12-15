from django import forms
from .models import PaintingRequest

class PaintingRequestForm(forms.ModelForm):
    class Meta:
        model = PaintingRequest
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 10, 'style': 'height: 100px;'}),
        }
