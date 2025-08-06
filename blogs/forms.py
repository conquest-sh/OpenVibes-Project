from django import forms

from .models import Overall,Explain

class OverallForm(forms.ModelForm):
    class Meta:
        model = Overall
        fields = ['name']
        labels = {'name': ''}

class ExplainForm(forms.ModelForm):
    class Meta:
        model = Explain
        fields = ['name']
        labels = {'name': ''}
        widgets = {'name': forms.Textarea(attrs={'cols': 80})}