from django.db import models
from django.contrib import admin

# Create your models here.

class characters(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()

admin.site.register(characters)

