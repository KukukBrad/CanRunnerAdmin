from django.db import models

# Create your models here.
class User(models.Model):
	full_name = models.CharField( primary_key=True, max_length=200)
	email = models.CharField(max_length=200)
	phone = models.CharField(max_length=200)
	assigned_route = models.CharField(max_length=200)

	def __str__(self):
		return self.full_name


class Property(models.Model):
	prop_name = models.CharField(max_length=200)
	street_address = models.CharField(primary_key=True, max_length=200)
	city = models.CharField(max_length=200)
	state = models.CharField(max_length=200)
	zip_code = models.IntegerField()
	pin_color = models.CharField(max_length=200)
	route = models.CharField(max_length =200)
	service_time = models.IntegerField()
	can_detail = models.CharField(max_length=200)
	action = models.CharField(max_length=200)
	notes = models.CharField(max_length=200)

	def __str__(self):
		return self.street_address
