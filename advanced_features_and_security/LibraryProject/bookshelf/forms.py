from django import forms

class ExampleForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
