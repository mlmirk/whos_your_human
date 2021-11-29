from django.db import models
from django.urls import reverse
from datetime import date
# Import the User
from django.contrib.auth.models import User
# Create your models here.

class Pet(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100,  null=True, blank=True )
  description = models.TextField(max_length=250,  null=True, blank=True)
  parent1 = models.CharField(max_length=100)
  parent2 = models.CharField(max_length=100,  null=True, blank=True)
  insta= models.CharField(max_length=100,  null=True, blank=True)
  play_date=models.BooleanField(null=True, blank=True)
  email= models.EmailField(max_length=254,  null=True, blank=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('pets_detail', kwargs={'pet_id': self.id})




class Photo(models.Model):
  url = models.CharField(max_length=250)
  pet = models.OneToOneField(Pet, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for pet_id: {self.pet_id} @{self.url}"

