from django import forms
from hello.models import Workout, Exercise

class FilterForm(forms.ModelForm):
    class Meta:
            model = Exercise
            fields = ("exercise",)

    def __init__(self, *args, **kwargs):
        super(FilterForm, self).__init__(*args, **kwargs)
        self.fields['exercise'].required = False

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
