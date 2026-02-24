from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div
from .models import Take, Problem


class TakeForm(forms.ModelForm):
    class Meta:
        model = Take
        fields = ('pain_level',
                  'frequency',
                  'affected_people',
                  'description',)

    # The clean_description method is a Django convention.
    # Any method named clean_<fieldname> on a ModelForm automatically runs as
    # validation for that field when is_valid() is called.
    # If the description is under 50 characters,
    # it raises a ValidationError which:
    # - Prevents the form from saving
    # - Makes the error message available in the template
    #  via {{take_form.description.errors}}

    def clean_description(self):
        description = self.cleaned_data.get('description', '')
        if len(description) < 50:
            raise forms.ValidationError(
                'Description must be at least 50 characters long.'
            )

        # In Django's clean_<fieldname> convention, the return value replaces
        # the value in cleaned_data for that field.
        # So when you return description, Django stores it back into
        # self.cleaned_data['description'].
        # This is the value that gets used later when you call
        # take_form.save() in your view
        # Django reads from cleaned_data to populate the model fields.
        return description


class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ('title',
                  'industry',
                  'job_role',
                  'pain_level',
                  'frequency',
                  'affected_people',
                  'description',
                  'workaround',
                  'contact_info',
                  'show_contact',
                  'is_solved',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False  # We handle <form> in the template
        self.helper.layout = Layout(
            # Row 1: Title (full width)
            Field('title', css_class='mb-3'),
            # Row 2: Industry + Job Role side by side
            Div(
                Field('industry', wrapper_class='col-md-6'),
                Field('job_role', wrapper_class='col-md-6'),
                css_class='row',
            ),
            # Row 3: Pain Level + Frequency + Affected People
            Div(
                Field('pain_level', wrapper_class='col-md-4'),
                Field('frequency', wrapper_class='col-md-4'),
                Field('affected_people', wrapper_class='col-md-4'),
                css_class='row',
            ),
            # Row 4: Description (full width)
            Field('description', rows=7),
            # Row 5: Workaround (full width)
            Field('workaround', rows=5),
            # Row 6: Contact info + checkboxes
            Div(
                Field('contact_info', wrapper_class='col-md-6'),
                Div(
                    Field('show_contact'),
                    Field('is_solved'),
                    css_class='col-md-6 d-flex align-items-end gap-4 mb-3',
                ),
                css_class='row',
            ),
        )

    def clean_description(self):
        description = self.cleaned_data.get('description', '')
        if len(description) < 50:
            raise forms.ValidationError(
                'Description must be at least 50 characters long.'
            )
        return description


class ProblemSubmitForm(ProblemForm):
    class Meta(ProblemForm.Meta):
        exclude = ('is_solved',)
