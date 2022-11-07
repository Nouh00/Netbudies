from distutils import text_file
from email.policy import default
from pyexpat import model
from turtle import update
from unicodedata import name
from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    name = models.CharField(max_length=100, null=True)
    email= models.CharField(unique=True, max_length=100, null=True)
    bio = models.TextField(null=True)

    avatar = models.ImageField(null=True, default="avatar.svg")

    USERNAME_FIELD = 'email'    
    REQUIRED_FIELDS = []

class Topic(models.Model):
    name= models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Create your models here.
class Room(models.Model):
    host = models.ForeignKey(User, on_delete= models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete= models.SET_NULL, null=True)
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']
    
    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete= models.CASCADE)
    body= models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']
        
    def __str__(self):
        return self.body