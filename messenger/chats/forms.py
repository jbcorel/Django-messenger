from django import forms
from django.core.exceptions import ValidationError
from .models import Room

 
class RoomCreationForm(forms.ModelForm):
    class Meta:
        model = Room 
        fields = ('name', 'slug', 'password', 'creator_id')
        widgets = {
            'password': forms.PasswordInput(render_value=True),
            'creator_id': forms.HiddenInput(),
        }
    
    def clean_creator_id(self):
        creator_id = self.cleaned_data.get('creator_id')
        if not creator_id:
            raise ValidationError('Creator ID is required.')
        return creator_id
        


        
    