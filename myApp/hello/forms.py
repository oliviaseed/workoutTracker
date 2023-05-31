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

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ("exercise","reps","val","specs",)   # NOTE: the trailing comma is required
        # widgets = {
        #     'exercise': forms.RadioSelect(),
        # }
