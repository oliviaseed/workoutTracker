from django import forms
from hello.models import Workout, Exercise

class entryForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ("exercise","reps","val","specs",)   # NOTE: the trailing comma is required

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        exclude = []
        #fields = ("",)   # NOTE: the trailing comma is required

class ExerciseForm(forms.ModelForm):
    #workout_id = forms.CharField(required=False)
    class Meta:
        model = Exercise
        fields = ("exercise","reps","val","specs",)   # NOTE: the trailing comma is required
