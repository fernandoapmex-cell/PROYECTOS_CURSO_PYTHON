from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import request

# Create your views here.
def bienvenido(request):
    return HttpResponse("hola mundo desde django")
def despedirse(args):
    return HttpResponse("Despedida desde django")
