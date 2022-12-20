from django import forms

class EmailForm(forms.Form):

    first_name = forms.CharField(label='First name', max_length=100)
    last_name = forms.CharField(label='Last name', max_length=100)
    email_address = forms.CharField(label='Email', max_length=100)