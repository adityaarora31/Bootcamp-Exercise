from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def greet_now(request, time_now):

    if time_now > 6 and time_now < 12:

        return HttpResponse("Good Morning !")

    elif time_now > 12 and time_now < 18:

        return HttpResponse("Good Afternoon !")

    elif time_now > 18 and time_now < 24:

        return HttpResponse("Good Night !")

    else:
        return HttpResponse("Go To Bed !")
