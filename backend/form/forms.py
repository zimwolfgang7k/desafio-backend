from django import forms


class Form(forms.Form):
    code = forms.CharField(max_length=255)
