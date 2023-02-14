from django import forms
from django.forms import DateField, NumberInput
from .models import register

requirement_choices = [
    ('', 'Select Type'),
    ('type1', 'Type 1 - Planetary transit'),
    ('type2', 'Type 2 - House warming'),
    ('type3', 'Type 3 - Telugu Sampradaya'),
    ('type4', 'Type 4 - Homam'),
    ('type5', 'Type 5 - Sirartha'),
    ('type6', 'Type 6 - As per Telugu tradition')
]

services_choices = [
    ('', 'Select Services'),
]

mode_choices = [
    ('0', 'Select Mode'),
    ('1', 'Offline'),
    ('2', 'Online')
]

class registerForm(forms.Form):
    first_name = forms.CharField(label = "First Name")
    last_name = forms.CharField(label = "Last Name")
    email = forms.EmailField(label="Email ID")
    phonenumber = forms.CharField(label="Contact Number")
    address = forms.CharField(widget = forms.Textarea(
        attrs={'placeholder': 'Address'}
        )
    )
    postalCode = forms.IntegerField(label="Postal Code")
    requirement = forms.ChoiceField(choices=requirement_choices, label="Requirement")
    services = forms.ChoiceField(choices=services_choices, label="Package")
    mode = forms.ChoiceField(choices=mode_choices, label="Mode")
    date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    others = forms.CharField(required = False, widget = forms.Textarea(
        attrs={'placeholder': 'Any other details, Please type in the box'}
        )
    )

class contactForm(forms.Form):
    first_name = forms.CharField(label = "First Name")
    last_name = forms.CharField(label = "Last Name")
    subject = forms.CharField(label="Subject")
    message = forms.CharField(required = False, widget = forms.Textarea(
        attrs={'placeholder': 'Please type here...'}
        )
    )