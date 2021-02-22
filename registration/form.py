from django import forms


class signUpForm(forms.Form):
    firstName = forms.CharField(required=True)
    lastName = forms.CharField(required=True)
    email = forms.CharField(required=True)
    password = forms.CharField(required=True)

