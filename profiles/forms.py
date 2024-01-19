from django import forms
from profiles.widgets import CustomClearableFileInput
from .models import UserProfile
from home.models import PaintingRequest, TemporaryPaintingRequest


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County or State, or Locality',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'profile-form-input'
            self.fields[field].label = False


class PaintingEditForm(forms.ModelForm):
    class Meta:
        model = PaintingRequest
        exclude = ['user']

    examples = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)
    examples2 = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)
 

class TemporaryPaintingEditForm(forms.ModelForm):
    class Meta:
        model = TemporaryPaintingRequest
        exclude = ['user']

    examples = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)
    examples2 = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)