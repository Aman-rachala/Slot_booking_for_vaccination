from operator import mod
from tkinter import Widget
from django.db import models
from django import forms

#CHOICES = [('M','Male'),('F','Female')]


# Create your models here.
class pmodel(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    age = models.IntegerField()
    username = models.EmailField(max_length=200)
    phno = models.CharField(max_length=13)
    # gender = models.CharField(max_length=1,default="M")
    pwd = models.CharField(max_length=20)
    repwd = models.CharField(max_length=20)

class hmodel(models.Model):
    hname = models.CharField(max_length=20,default=None)
    email = models.EmailField(max_length=50,default=None)    
    addr = models.CharField(max_length=100,default=None)
    slots = models.IntegerField(default=20)

