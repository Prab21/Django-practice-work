from __future__ import unicode_literals
from django.db import models

# Create your models here.


# created by purushottam prabhakar in the learning of django project of e commerce

class profile(models.Model):
	name= models.CharField(max_length=120)
	description = models.TextField(default='This is default text given by purushottam for testing purpose.',blank=True)
	location= models.CharField(max_length=120, default='my location default',null=True)
	job= models.CharField(max_length=120, null=True,blank=True)
	
	def __unicode(self):
		return self.name
		
