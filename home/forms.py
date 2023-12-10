from django import forms
from .models import PaintingRequest

class PaintingRequestForm(forms.ModelForm):

    class Meta:
        model = PaintingRequest
        fields = '__all__'
