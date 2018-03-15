from django import forms
from .models import GuestList


class RegisterForm(forms.ModelForm):

    class Meta:

        model = GuestList
        fields = [
            'first_name',
            'last_name',
            'title',
            'message',
            'image',
        ]


