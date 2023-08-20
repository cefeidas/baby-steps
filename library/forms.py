# forms.py
from django import forms

class SearchBookForm(forms.Form):
    query = forms.CharField(required=True, label="Search:")
    field = forms.ChoiceField(choices=[('title', 'Title'), ('writer', 'Writer')]) # Add other fields as needed
