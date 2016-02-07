# -*- coding: utf-8 -*-
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.admin.widgets import AdminDateWidget 

class HobbsForm(forms.Form):

    text = forms.CharField(
        widget=forms.TextInput(attrs=dict(required=False, max_length=500, render_value=False)),
        required=False,
        label=('Enter the sentence/paragraph')
    )

    pronoun = forms.CharField (
        label = 'Enter the pronoun'
    )

    docfile = forms.FileField(
        label='Upload a parse tree file',
        required=False
    )
