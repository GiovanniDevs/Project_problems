from .models import Take
from django import forms


class TakeForm(forms.ModelForm):
    class Meta:
        model = Take
        fields = ('pain_level',
                  'description',
                  'frequency',
                  'affected_people',)
