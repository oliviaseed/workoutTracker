from django.urls import path
from hello import views
from hello.models import LogMessage, Workout, Exercise

# home_list_view = views.HomeListView.as_view(
#     queryset=LogMessage.objects.order_by("-log_date")[:5],  # :5 limits the results to the five most recent
#     context_object_name="message_list",
#     template_name="hello/home.html",
# )

home_list_view = views.HomeListView.as_view(
    queryset=Workout.objects.order_by("id")[:5],  # :5 limits the results to the five most recent
    context_object_name="workout_list",
    template_name="hello/home.html",
)

exercise_list_view = views.HomeListView.as_view(
    queryset=Exercise.objects.order_by("id")[:5],  # :5 limits the results to the five most recent
    context_object_name="exercise_list",
    template_name="hello/history.html",
)

urlpatterns = [
    path("", home_list_view, name="home"),
    path("history", exercise_list_view, name="history"),
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("log/", views.log_message, name="log"),
    path("exercise/", views.logExercise, name="exercise"),

]

