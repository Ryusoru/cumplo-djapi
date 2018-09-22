from django import forms
from functools import partial

from . import models

class QueryForm(forms.ModelForm):
    class Meta:
        model = models.Query
        fields = (
            'start_date',
            'end_date',
            'finantial_indicators'
        )
        widgets = {
            'start_date': forms.DateInput(attrs={'class': 'datepicker'}),
            'end_date': forms.DateInput(attrs={'class': 'datepicker'}),
            'finantial_indicators': forms.CheckboxSelectMultiple,
        }
        labels = {
            'start_date':'Since',
            'end_date':'To',
        }
