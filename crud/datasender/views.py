import json
import os
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def file_maker(request):

    if request.method == 'POST':
        json_data = request.body.decode('utf-8')
        data = json.loads(json_data)
        filename = data['file_name']
        content = data['content']

        with open(filename, "w+") as myfile:
            myfile.write(content)

    return HttpResponse("Done!")



def file_reader(request, filename):
    if request.method == 'GET':

        with open(filename, "r+") as myfile:
            data = myfile.read()
            return HttpResponse(data)


def file_updater(request, filename):
    if request.method == 'PUT':
        json_data = request.body.decode('utf-8')
        data = json.loads(json_data)
        with open(filename, "r+") as myfile:

            myfile.write(data['content'])
            return HttpResponse("Updated !")


def file_deleter(request, filename):
    if request.method == 'DELETE':
        try:
            os.remove(filename)
        except FileNotFoundError as error:
            print("Error is {}". format(error))
            exit()
    return HttpResponse("Deleted !")
