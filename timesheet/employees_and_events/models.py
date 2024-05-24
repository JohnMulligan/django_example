from django.db import models

# Create your models here.

#PEOPLE
class Person(models.Model):
	first_name=models.CharField(max_length=100)
	surname=models.CharField(max_length=100)
	assigned_card=models.ForeignKey(
		'Card',
		on_delete=models.SET_NULL,
		null=True
	)
	assigned_department=models.ForeignKey(
		'Department',
		on_delete=models.SET_NULL,
		null=True
	)
	def __str__(self):
		return f'{self.first_name} {self.surname}'

#CARDS
class Card(models.Model):
	card_number=models.CharField(
		max_length=100,
		unique=True
	)
	card_designation=models.CharField(
		max_length=100,
		unique=True
	)
	assigned_department=models.ForeignKey(
		'Department',
		on_delete=models.SET_NULL,
		null=True
	)
	def __str__(self):
		return f'{self.card_designation}: {self.card_number}'

valid_event_types=[
	("ClockIn","Clock In"),
	("ClockOut","Clock Out")
]

#EVENTS
class Event(models.Model):
	date_time=models.DateTimeField(auto_now_add=True)
	event_type=models.CharField(
		max_length=20,
		choices=valid_event_types
	)
	card_used=models.ForeignKey(
		Card,
		on_delete=models.SET_NULL,
		null=True
	)
	associated_person=models.ForeignKey(
		Person,
		on_delete=models.SET_NULL,
		null=True
	)
	def __str__(self):
		return f'{self.event_type}: {self.card_used}, {self.associated_person}'
	
#DEPARTMENTS
class Department(models.Model):
	name=models.CharField(max_length=100,unique=True)
	
	def __str__(self):
		
		return self.name
		
	
	
	
	
	
	
	
	
	
	
	
	
	
	