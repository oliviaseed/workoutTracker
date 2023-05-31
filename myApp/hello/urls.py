from django.urls import path
from hello import views
from hello.models import Workout, Exercise

workout_list_view = views.MyWorkoutView.as_view(
    queryset=Workout.objects.order_by("id")[:5],  # :5 limits the results to the five most recent
    context_object_name="workout_list",
    template_name="hello/home.html",
)

exercise_list_view = views.MyWorkoutView.as_view(
    queryset=Exercise.objects.order_by("id"),  # :5 limits the results to the five most recent
    context_object_name="exercise_list",
    template_name="hello/history.html",
)

urlpatterns = [
    path("", workout_list_view, name="home"),
    path("history", exercise_list_view, name="history"),
    path("exercise/", views.dynamic, name="exercise"),
]

