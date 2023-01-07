from django import forms
from .models import UsersList, UserMessages


# class FormName(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()
#     text = forms.CharField(widget=forms.Textarea)


class NewUser(forms.ModelForm):
    class Meta:
        model = UsersList
        fields = '__all__'


class UserMessage(forms.ModelForm):
    class Meta:
        model = UserMessages
        fields = '__all__'
