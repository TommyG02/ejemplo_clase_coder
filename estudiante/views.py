from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime

def saludar(request):
    return HttpResponse(f'Hola Mundo !! Hora: {datetime.now()}')


