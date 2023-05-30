from django import forms
from hello.models import Exercise

class entryForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ("exercise","reps","val","specs",)   # NOTE: the trailing comma is required
