
#from django.http import HttpResponse
from django.shortcuts import render, redirect
from hello.forms import WorkoutForm, ExerciseForm, FilterForm
from hello.models import Workout, Exercise
from django.views.generic import ListView

class MyWorkoutView(ListView):
    model = Exercise

    def get_context_data(self, **kwargs):
        context = super(MyWorkoutView, self).get_context_data(**kwargs)
        return context
    
def home(request):
    workout_list_view = Workout.objects.filter(status=True).order_by("id")
    if request.method == "POST" and request.POST.get('details'):
        return redirect('specific_workout', request.POST.get('details'))
    else:
        print('rendering all workouts:',workout_list_view)
        return render(request,'hello/home.html',{'workout_list': workout_list_view})

def history(request):
    exercise_list_view = Exercise.objects.order_by("workout_id") #most recent first
    if request.method == "POST":
        if request.POST.get('exercise') != (None or ''):
            filter = request.POST.getlist('exercise')
            exercise_list_view = Exercise.objects.filter(exercise=filter[0]).order_by("workout_id")

    return render(request,'hello/history.html',{'exercise_list': exercise_list_view, 'filter_form': FilterForm()})

def getWorkout(request, id):
    print(f'Requesting workout with id:{id}')
    exercise_list_view = Exercise.objects.filter(workout_id=id)
    print(f'exercise_list_view:{exercise_list_view}')
    return render(request,'hello/history.html',{'exercise_list': exercise_list_view})

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
            return redirect('workout')
        elif request.POST.getlist('log'): 
            print('test')
            exercise_form = ExerciseForm(request.POST)
            if exercise_form.is_valid():
                exercise = exercise_form.save(commit=False)
                exercise.workout_id = workout.id
                exercise.details = str(exercise.val)+' '+exercise.specs
                print(f'exercise:{exercise}')
                existing = Exercise.objects.filter(workout_id=workout.id,exercise=exercise.exercise, details=exercise.details).last()
                print(f'existing:{existing}')
                if existing: 
                    print('existing.sets:',existing.sets)
                    existing.sets += 1     
                    existing.save()               
                else:
                    exercise = exercise_form.save(commit=False)
                    exercise.workout_id = workout.id
                    exercise.details = str(exercise.val)+' '+exercise.specs
                    exercise.save()
            context['exercise_form'] = exercise_form
        elif request.POST.getlist('end'):
            Workout.objects.filter(status=False).last().endWorkout().save()
            return redirect('home')
    else: print('lol F')
    return render(request, "hello/logExercise.html", context)