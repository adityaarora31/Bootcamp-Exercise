from django.contrib import admin
from django.urls import path
from .views import EmployeeList, EmployeeDetail, EmployeeUpdate, EmployeeDelete, EmployeeCreate

urlpatterns = [
    # path('app/', ContactView.as_view()),
    path('get/', EmployeeList.as_view(), name='abcd'),
    path('get_detail/<int:pk>/', EmployeeDetail.as_view()),
    path('update_employee/<int:pk>/', EmployeeUpdate.as_view()),
    path('delete_employee/<int:pk>/', EmployeeDelete.as_view()),
    path('create_employee/', EmployeeCreate.as_view()),
]