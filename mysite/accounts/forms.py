from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField

from .models import Profile

# Form for a user to sign up.
class UserForm(UserCreationForm):
    # Sets placeholders for specified fields.
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['phone_number'].widget.attrs['placeholder'] = 'eg. +1 111 111 1111'

    phone_number = PhoneNumberField()
    
    # Overrides Django's default save method because I need to account for extended User model.
    def save(self):
        user = super(UserForm, self).save()
        profile = Profile(
            user = user,
            phone_number = self.cleaned_data['phone_number'],
        )
        profile.save()

        return user, profile


    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'phone_number']
        # fields = ['username', 'password1', 'password2']