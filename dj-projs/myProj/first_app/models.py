from django.db import models

# Create your models here.
class Members(models.Model):
	first_name = models.CharField(max_length=255) #text field to contain first names
	last_name = models.CharField(max_length=255) #text fields to contain last names
