from django.urls import path, include
from .views import *


urlpatterns = [
    path('index/<int:time_now>/', greet_now, name="greet")
]
