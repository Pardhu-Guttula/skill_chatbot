from django import forms

class UserInputForm(forms.Form):
    user_input = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 47}))
