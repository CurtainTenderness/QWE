from django import forms

class UserFrom(forms.Form):
    name=forms.CharField(max_length=40,min_length=2)
    age=forms.IntegerField(label='年龄')