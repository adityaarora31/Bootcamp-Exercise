from django.db import models

# Create your models here.
from django.urls import reverse


class Employee(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('abcd')