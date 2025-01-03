from django import forms

from .models import Sport, Entry

class SportForm(forms.ModelForm):
    class Meta:
        model = Sport
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ' '}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}