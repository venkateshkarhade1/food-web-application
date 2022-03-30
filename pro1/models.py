from email.policy import default
from tabnanny import verbose
from django.db import models
from django.conf import settings

from django.shortcuts import reverse

import stripe
import uuid

class descr(models.Model):
    name=models.CharField(max_length=100)
    dec=models.TextField()
    price=models.IntegerField()
    image=models.ImageField(upload_to='pics')
    pname=models.TextField()
  
    