import datetime

from django.db import models
from django.utils import timezone

# Create your models here
class Shift(models.Model):
	time_start = models.DateTimeField('Start Time')
	time_end = models.DateTimeField('End Time')
	location = models.CharField(max_length=200)
	physician = models.CharField(max_length=200)


	def __str__(self):
		return self.shift_location


class Physician(models.Model):
	id = models.AutoField(primary_key=True)
	name_first = models.CharField(max_length=200)
	name_last = models.CharField(max_length=200)
	specialty = models.CharField(max_length=200)

	def __str__(self):
		return self.name_first + " " + self.name_last
class Specialty(models.Model):
	def __str__(self):
		return ''
class Appointment(models.Model):
	def __str__(self):
		return ''

class Patient(models.Model):
	def __str__(self):
		return ''

class Procedure(models.Model):
	def __str__(self):
		return ''
