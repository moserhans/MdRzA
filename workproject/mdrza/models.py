from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class radler(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	vname = models.CharField(max_length=100)
	nname = models.CharField(max_length=100)
	email = models.EmailField(max_length=100)
	team = models.ForeignKey('mdrza.team',null=True, related_name='members')
	km = models.PositiveSmallIntegerField(null=True)
	gesamtkm = models.PositiveSmallIntegerField(null=True)
	gesamttage = models.PositiveSmallIntegerField(null=True,default=0)
	def __unicode__(self):
		return self.email

class team(models.Model):
	name = models.CharField(max_length=100)
	gesamtkm = models.PositiveSmallIntegerField(null=True)
	def __unicode__(self):
		return self.name

class woche(models.Model):
	kwnr = models.IntegerField()
	user = models.ForeignKey('mdrza.radler', related_name='weeks')
	mo = models.BooleanField(default=False)
	di = models.BooleanField(default=False)
	mi = models.BooleanField(default=False)
	do = models.BooleanField(default=False)
	fr = models.BooleanField(default=False)
	mo_extra = models.PositiveSmallIntegerField(null=True,default=0)
	di_extra = models.PositiveSmallIntegerField(null=True,default=0)
	mi_extra = models.PositiveSmallIntegerField(null=True,default=0)
	do_extra = models.PositiveSmallIntegerField(null=True,default=0)
	fr_extra = models.PositiveSmallIntegerField(null=True,default=0)
	km = models.PositiveSmallIntegerField(null=True,default=0)
	def __str__(self):
		kwnr = str(self.kwnr)
		return kwnr
