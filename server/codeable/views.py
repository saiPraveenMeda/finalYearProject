from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, render_to_response, redirect
import json
import subprocess

def temp(request) :
    subprocess.Popen(['/home/sai/Desktop/project_temp/temp2.sh'], shell=True)
    result = 'Success'
    return HttpResponse(result)