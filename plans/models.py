from django.db import models

# Create your models here.


PLAN_TYPE =  (
    ("Mobile", "Mobile"),
    ("Dish", "Dish"),
    ("Electricity", "Electricity"),
)

class Plan(models.Model):
	name = models.CharField(max_length=40)
	plan_type = models.CharField(max_length=20, choices=PLAN_TYPE)
	operator = models.CharField(max_length=20)
	city = models.CharField(max_length=40)
	days = models.CharField(max_length=10)
	amount = models.PositiveIntegerField()
	date_added = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=True)

	def __str__(self):
		return str(self.id)