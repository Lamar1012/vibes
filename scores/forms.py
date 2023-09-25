import phonenumbers
from phonenumbers import is_valid_number, parse 
from django import forms
from django.forms import ModelForm
from .models import User

regex=r'^\+?1?\d{9,15}$'
class SubscriberForm(ModelForm):
    phone_number = forms.CharField(widget= forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Enter Phone Number'}), initial='+1')
    class Meta():
        model = User
        fields = ('phone_number',)
        labels =  {'phone_number': ''}
        

    
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        try:
            parsed_number = parse(phone_number, None)
        except phonenumbers.phonenumberutil.NumberParseException:
            raise forms.ValidationError("Enter a valid phone number")

        # Check if the parsed number is valid
        if not is_valid_number(parsed_number):
            raise forms.ValidationError("Enter a valid phone number")

        return phone_number