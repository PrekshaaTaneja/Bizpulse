from django import forms
from .models import emails

class EmailForm(forms.ModelForm):
    class Meta:
        model = emails
        fields = ['email']