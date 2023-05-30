
#from django.http import HttpResponse
from django.shortcuts import render
import datetime
#from django.utils import timezone
from django.shortcuts import redirect
from hello.forms import entryForm
from hello.models import Workout, Exercise
from django.views.generic import ListView
#from django.contrib.sessions.models import Session
#from django.contrib.sessions.backends.db import SessionStore

    
class MyWorkoutView(ListView):
    model = Exercise

    def get_context_data(self, **kwargs):
        context = super(MyWorkoutView, self).get_context_data(**kwargs)
        return context
    
def about(request):
    return render(request, "hello/about.html")

def contact(request):
    return render(request, "hello/contact.html")

def hello_there(request, name):
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )
    
def logExercise(request):
    form = entryForm(request.POST or None)
    request.session.get('inSession', False) #set default
    if request.method == "POST" and 'log' in request.POST:
        # start new workout :)
        if  request.session.get('inSession', False) == False:
            workout = Workout()
            workout.save() #now in database
            request.session["inSession"] = True #TODO: edit navbar conditions
            request.session["startTime"] = workout.id

        if form.is_valid():
            exercise = form.save(commit=False)
            #exercise.id = timezone.datetime.now()
            exercise.details = str(exercise.val)+exercise.specs
            exercise.save()
            return redirect("home")
    
    # end workout
    elif request.method == "POST" and 'end' in request.POST:
        if request.session["inSession"]:
            print(f'LF Workout with startTime:{request.session["startTime"]}')
            workout = Workout.objects.filter(id=request.session["startTime"]).first().endWorkout()
            workout.save()
            request.session["inSession"] = False
            return redirect("home")
        else:
            return render(request, "hello/logExercise.html", {"form": form})
    else:
        exercise_list = MyWorkoutView.as_view(
            queryset=Exercise.objects.filter(id=request.session["startTime"])[:5],  # :5 limits the results to the five most recent
            context_object_name="exercise_list",
            template_name="hello/history.html",
        )
        return render(request, "hello/logExercise.html", {"form": form,'table':exercise_list})
    