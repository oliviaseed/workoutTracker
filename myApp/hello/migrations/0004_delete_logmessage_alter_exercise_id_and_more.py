# Generated by Django 4.2.1 on 2023-05-30 13:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_exercise_details_exercise_reps_exercise_specs_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LogMessage',
        ),
        migrations.AlterField(
            model_name='exercise',
            name='id',
            field=models.CharField(default='01:18:29', max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='workout',
            name='date',
            field=models.DateField(default=datetime.date(2023, 5, 31)),
        ),
        migrations.AlterField(
            model_name='workout',
            name='id',
            field=models.CharField(default='01:18:29', max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='workout',
            name='time_end',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 31, 1, 18, 29, 56362)),
        ),
        migrations.AlterField(
            model_name='workout',
            name='time_start',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 31, 1, 18, 29, 56362)),
        ),
    ]