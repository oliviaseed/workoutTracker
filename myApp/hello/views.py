
#from django.http import HttpResponse
from django.shortcuts import render
import datetime
#from django.utils import timezone
from django.shortcuts import redirect
from hello.forms import entryForm, WorkoutForm, ExerciseForm
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
    val = request.session.get('inSession', False) #set default
    id = request.session.get('id', False) #set default

    print(f'IN SESH:{val} with ID:{id}')
    if request.session.get('inSession', False)==True:
        print(request.session.get('id', False))
        exercise_list = Exercise.objects.filter(workout_id=request.session["id"])
    else:
        exercise_list=0
    print(f'TEST:\n{exercise_list}')
    
    #log set
    if request.method == "POST" and 'log' in request.POST:   
        # start new workout :)
        if  request.session.get('inSession', False) == False:
            print('Starting new workout!')
            workout = Workout()
            workout.create()
            workout.save() #now in database
            request.session["inSession"] = True #TODO: edit navbar conditions
            request.session["id"] = workout.id

        if form.is_valid():
            exercise = form.save(commit=False)
            #exercise.create() 
            exercise.workout_id = request.session["id"]
            exercise.details = str(exercise.val)+exercise.specs
            exercise.save()
            return redirect("exercise")
            return render(request, "hello/logExercise.html", {"form": form,'exercise_list':exercise_list})
    
    # end workout
    elif request.method == "POST" and 'end' in request.POST:
        if request.session["inSession"]:
            print(f'LF Workout with id:{request.session["id"]}')
            workout = Workout.objects.filter(id=request.session["id"]).first().endWorkout()
            workout.save()
            request.session["inSession"] = False
            return redirect("home")
        else:
            return render(request, "hello/logExercise.html", {"form": form,'exercise_list':exercise_list})
    else:
        return render(request, "hello/logExercise.html", {"form": form,'exercise_list':exercise_list})
    
def dynamic(request):
    context = {}
    workout = Workout.objects.filter(status=False).last()

    if (request.method == "GET" or "POST"):
        if Workout.objects.filter(status=False).last() == None:
            context['workout_form'] = WorkoutForm() 
        else:
            context['exercise_list'] = Exercise.objects.filter(workout_id=workout.id)
            if Exercise.objects.filter(workout_id=workout.id):
                context['exercise_form'] = ExerciseForm(instance=Exercise.objects.filter(workout_id=workout.id).last())
            else: context['exercise_form'] = ExerciseForm()
    
    if (request.method == "POST"):
        print(f'request.POST:{request.POST}')
        if request.POST.get('workout'): 
            context['workout_form'] = None 
            Workout.objects.create().save()
            return redirect('exercise')
        elif request.POST.getlist('log'): 
            print('test')
            exercise_form = ExerciseForm(request.POST)
            if exercise_form.is_valid():
                exercise = exercise_form.save(commit=False)
                exercise.workout_id = workout.id
                exercise.details = str(exercise.val)+exercise.specs
                exercise.save()
            context['exercise_form'] = exercise_form
        elif request.POST.getlist('end'):
            Workout.objects.filter(status=False).last().endWorkout().save()
            return redirect('home')
    else: print('lol F')
    return render(request, "hello/logExercise.html", context)