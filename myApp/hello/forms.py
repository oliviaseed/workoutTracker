from django import forms
from hello.models import LogMessage
from hello.models import Exercise

class LogMessageForm(forms.ModelForm):
    class Meta:
        model = LogMessage
        fields = ("message",)   # NOTE: the trailing comma is required

class entryForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ("exercise","reps","val","specs",)   # NOTE: the trailing comma is required
