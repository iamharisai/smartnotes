from django import forms
from django.core.exceptions import ValidationError

from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text')

    def clean_text(self):
        text = self.cleaned_data['text']
        if 'Django' not in text:
            raise ValidationError('We only accept notes about Django!')
        return text