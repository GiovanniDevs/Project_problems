from .models import Take
from django import forms


class TakeForm(forms.ModelForm):
    class Meta:
        model = Take
        fields = ('pain_level',
                  'description',
                  'frequency',
                  'affected_people',)

    # The clean_description method is a Django convention.
    # Any method named clean_<fieldname> on a ModelForm automatically runs as
    # validation for that field when is_valid() is called.
    # If the description is under 50 characters, it raises a ValidationError which:
    # - Prevents the form from saving
    # - Makes the error message available in the template via {{take_form.description.errors}}

    def clean_description(self):
        description = self.cleaned_data.get('description', '')
        if len(description) < 50:
            raise forms.ValidationError(
                'Description must be at least 50 characters long.'
            )

        # In Django's clean_<fieldname> convention, the return value replaces
        # the value in cleaned_data for that field. So when you return description,
        # Django stores it back into self.cleaned_data['description'].
        # This is the value that gets used later when you call take_form.save() in your view —
        # Django reads from cleaned_data to populate the model fields.
        return description
