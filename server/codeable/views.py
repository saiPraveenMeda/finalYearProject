from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, render_to_response, redirect
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
import json,os
import subprocess
from .serializers import FileSerializer
from django.core.files.storage import FileSystemStorage

def temp(request) :
    subprocess.Popen(['/home/sai/Desktop/project_temp/temp2.sh'], shell=True)
    result = 'Success'
    response = {}
    return render(request,'codeable/temp.djt',response)

def FileView(request):
    folder='my_folder/' 
    if request.method == 'POST' and request.FILES['file']:
        myfile = request.FILES['file']
        fs = FileSystemStorage(location=folder) #defaults to   MEDIA_ROOT  
        filename = fs.save(myfile.name, myfile)
        file_url = fs.url(filename)
        return HttpResponse('file_url=' + file_url)
    else:
         return HttpResponse('some error occured')