from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    desc = models.TextField()


class Problem(models.Model):
    question = models.TextField()
    feedback = models.TextField()