from django import forms


class UserInputForm(forms.Form):
    user_input = forms.CharField(widget=forms.TextInput(attrs={"rows": 2, "cols": 47}))
