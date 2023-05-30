from typing import Any
from django.db import models
from django.utils import timezone
import datetime
from datetime import timedelta
#from django.utils.timezone import datetime

class LogMessage(models.Model):
    message = models.CharField(max_length=300)
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"
    
##mine

class Workout(models.Model):
    id = models.CharField(primary_key=True, max_length=100, default=datetime.datetime.now().strftime("%H:%M:%S"))
    date = models.DateField(default=datetime.datetime.now().date())
    time_start = models.DateTimeField(default=datetime.datetime.now())
    time_end = models.DateTimeField(default=datetime.datetime.now())
    length = models.DurationField(default=timedelta())
    print(f'INSTANTIATED Workout at {datetime.datetime.now().strftime("%H:%M:%S")}')

    def create(self):
        self.time_start = datetime.datetime.now()
        self.date = self.time_start.date()
        self.id = self.time_start.strftime("%H:%M:%S")
        print(f'Initited Workout with id:{self.id}')
    
    def endWorkout(self):
        self.time_end = timezone.make_aware(datetime.datetime.now() )#NAIVE!
        self.length = self.time_end-self.time_start
        print(f'Ended Workout.')
        return self


class Set(models.Model):
    _id = models.IntegerField() #chronological (set 1, 2, ...)
    type = models.CharField(max_length=300, choices=[('wa', 'warmup'),('wo', 'working')]) 
    reps = models.IntegerField()
    UNIT_OPTIONS = [('kg', 'kg'),('lb','lb'),('s','seconds'),('min', 'minutes')]
    specs = models.CharField(max_length=3, choices=UNIT_OPTIONS) 

class Exercise(models.Model):
    id = models.CharField(primary_key=True, max_length=100, default=datetime.datetime.now().strftime("%H:%M:%S"))
    
    def create(self):
        self.id=datetime.datetime.now().strftime("%H:%M:%S")
    
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
    exercise = models.CharField(max_length=3, choices=EXERCISE_CATEGORIES) 

    reps = models.IntegerField(default='10')
    val = models.IntegerField(default='0')
    UNIT_OPTIONS = [('kg', 'kg'),('lb','lb'),('s','seconds'),('min', 'minutes')]
    specs = models.CharField(max_length=3, choices=UNIT_OPTIONS, default=('kg', 'kg')) 
    details = models.CharField(max_length=10, default='')

    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"

class Note(models.Model):
   # _id = 0 
    exercise = models.CharField(max_length=300)
    note = []