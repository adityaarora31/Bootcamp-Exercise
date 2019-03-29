from django.db import models

# Create your models here.


class Manager(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    department = models.CharField(max_length=50)
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    salary = models.IntegerField()
    designation = models.CharField(max_length=50)
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
    reporting_manager = models.ForeignKey(Manager, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
