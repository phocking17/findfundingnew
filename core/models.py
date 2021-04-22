from django.db import models
from localflavor.us.us_states import STATE_CHOICES
import os


def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)


### All tags


class Tag_Type(models.Model):
	name=models.CharField(max_length=50)
	question = models.CharField(max_length=500)
	option_type = models.CharField(max_length=5)

	def __str__(self):
		s = self.name
		return s

class Technology_Tag(models.Model):
	name=models.CharField(max_length=50)
	def __str__(self):
		s = self.name
		return s


class Tag(models.Model):
	name=models.CharField(max_length=50)
	tag_type=models.ManyToManyField(Tag_Type)
	def __str__(self):
		s = self.name
		return s


class Contact (models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	email = models.EmailField()
	phone = models.CharField(max_length=10)
	def __str__(self):
		s = self.first_name + ' ' + self.last_name
		return s




class Organization (models.Model):
	name = models.CharField(max_length=200)
	city=models.CharField(max_length=100, blank=True)
	state= models.CharField(blank=True, max_length=2, choices=STATE_CHOICES)
	affiliations = models.ForeignKey('Organization',null=True,blank=True, on_delete=models.PROTECT)
	description = models.CharField(max_length=1000)
	website=models.URLField(max_length=500)
	org_image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
	contact = models.ManyToManyField(Contact, blank=True)
	def __str__(self):
		s = self.name
		return s



# Create your models here.
class Program(models.Model):
	name = models.CharField(max_length=200)
	city=models.CharField(max_length=100, blank=True)
	state= models.CharField(blank=True, max_length=2, choices=STATE_CHOICES)
	affiliations = models.ManyToManyField(Organization, blank=True)
	description = models.CharField(max_length=1000)
	focus=models.ManyToManyField(Tag, blank=True)
	technology_tags = models.ManyToManyField(Technology_Tag, blank=True)
	program_link=models.URLField(max_length=500)
	program_image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
	contact = models.ManyToManyField(Contact, blank=True)
	dates = models.DateField()

	def __str__(self):
		s = self.name
		return s


class Award (models.Model):
	name = models.CharField(max_length=200)
	amount = models.IntegerField()
	description = models.CharField(max_length=1000)
	program = models.ManyToManyField(Program)
	def __str__(self):
		s = self.name
		return s


class Response(models.Model):
	tags_selected=models.ManyToManyField(Tag)
	tags_completed=models.ManyToManyField(Tag_Type)
	overall_tags_selected=models.ManyToManyField(Technology_Tag)