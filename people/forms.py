from tkinter import Widget
from django import forms
from people.models import Person


class PersonF(forms.ModelForm):
    
    class Meta:
        model = Person
        fields = ("__all__")