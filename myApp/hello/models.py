from typing import Any
from django.db import models
from django.utils import timezone
import datetime
from datetime import timedelta
#from django.utils.timezone import datetime

class Workout(models.Model):
    id = models.CharField(primary_key=True, max_length=100, default=datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
    date = models.DateField(default=datetime.datetime.now().date())
    time_start = models.DateTimeField(default=timezone.make_aware(datetime.datetime.now()))
    time_end = models.DateTimeField(default=timezone.make_aware(datetime.datetime.now()))
    length = models.FloatField(default=0)
    status = models.BooleanField(default=False)
    print(f'INSTANTIATED Workout at {datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}')

    def create(self):
        self.time_start = timezone.make_aware(datetime.datetime.now())
        self.date = self.time_start.date()
        self.id = self.time_start.strftime("%m/%d/%Y, %H:%M:%S")
        print(f'Initited Workout with id:{self.id}')
    
    def endWorkout(self):
        self.time_end = timezone.make_aware(datetime.datetime.now())#NAIVE!
        self.length = (self.time_end-self.time_start).total_seconds() 
        self.status=True
        print(f'Ended Workout at {self.time_end} of length {self.length}s.')
        return self

class Set(models.Model):
    _id = models.IntegerField() #chronological (set 1, 2, ...)
    type = models.CharField(max_length=300, choices=[('wa', 'warmup'),('wo', 'working')]) 
    reps = models.IntegerField()
    UNIT_OPTIONS = [('kg', 'kg'),('lb','lb'),('s','seconds'),('min', 'minutes')]
    specs = models.CharField(max_length=3, choices=UNIT_OPTIONS) 

class Exercise(models.Model):
    workout_id = models.CharField(unique=False, max_length=100, default=datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
    
    def create(self):
        self.workout_id=datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    
    EXERCISE_CATEGORIES = [
    ('legs', (
        ('ht', 'hip thrust'),
        ('kas', 'kas glute bridge'),
        ('sht', 'single-leg hip thrust'),
        ('be', 'back extension'),
        ('s', 'squat'),
        ('bss', 'BSS'),
        ('rdl', 'RDL'),
        ('dl', 'deadlift'),
        ('su', 'step-ups'),
    )),
    ('upper-body', (
        ('bc', 'bicep curls'),
        ('hc', 'hammer curls'),
        ('pu', 'pull-ups'),
    )),
    ('abs', (
        ('io', 'in-n-outs'),
        ('pl', 'plank'),
        ('spl', 'side plank'),
        ('hd', 'hip dips'),
        ('vs', 'v-sit'),
    )),
    ('cardio', (
        ('jo', 'jo'),
        ('bi', 'bike'),
        ('st', 'stair master'),
    )),]
    exercise = models.CharField(max_length=30, choices=EXERCISE_CATEGORIES) 

    reps = models.IntegerField(default='10')
    val = models.IntegerField(default='0')
    UNIT_OPTIONS = [('kg', 'kg'),('lb','lb'),('s','seconds'),('min', 'minutes')]
    specs = models.CharField(max_length=3, choices=UNIT_OPTIONS, default=('kg', 'kg')) 
    details = models.CharField(max_length=10, default='')

    # def __str__(self):
    #     """Returns a string representation of a message."""
    #     date = timezone.localtime(self.log_date)
    #     return f"'{self.id}' created."

class Note(models.Model):
   # _id = 0 
    exercise = models.CharField(max_length=300)
    note = []