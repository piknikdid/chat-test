from django import forms
from .models import Chat
from django.contrib.auth.models import User

class HomeForm(forms.ModelForm):
    chat_text = forms.CharField()

    class Meta:
        model = Chat
        fields = ('chat_text',)

    def __init__(self, *args, **kwargs):
        super(HomeForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class RegForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ['username','email','password']
