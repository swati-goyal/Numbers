from django import forms
from .models import NumValue


class NumberForm(forms.ModelForm):
    number_value = forms.IntegerField(help_text="Enter a positive integer: ")
    number_property = forms.CharField(widget=forms.HiddenInput(), initial='')

    class Meta:
        model = NumValue
        fields = ('number_value',)
