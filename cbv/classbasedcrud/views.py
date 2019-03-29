from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .forms import ContactForm
from .models import Employee


# class ContactView(FormView):
#     template_name = 'contact.html'
#     form_class = ContactForm
#     model = Employee
#     success_url = '/thanks/'
#
#     def send_email(self, form):
#         form.send_email()
#         return super().form_valid(form)


class EmployeeList(ListView):
    model = Employee


class EmployeeDetail(DetailView):
    model = Employee


class EmployeeUpdate(UpdateView):
    model = Employee
    fields = ['name', 'designation']


class EmployeeDelete(DeleteView):
    model = Employee
    success_url = '/admin'


class EmployeeCreate(CreateView):
    model = Employee
    fields = ['name', 'designation']
    success_url = reverse_lazy('abcd')
