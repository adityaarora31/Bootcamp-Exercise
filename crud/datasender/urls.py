
from django.urls import path
from .views import *

urlpatterns = [
    path('datasender/', file_maker, name="file_maker"),
    path('datareader/<filename>/', file_reader, name="file_reader"),
    path('dataupdater/<filename>', file_updater, name="file_updater"),
    path('filedeleter/<filename>', file_deleter, name='file_deleter'),

]
