from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import request

from personas.models import Persona


# Create your views here.
def bienvenido(request):
    mensaje={'msg1':'Valor mensaje 1', 'msg2':'Valor mensaje 2'}
    #obtendremos los valores de la base de datos
    numero_personas=Persona.objects.count()
    personas=Persona.objects.order_by('id','nombre')
    #tambien se puede pasar directamente el dic
    return render(request,'bienvenido.html',{'numero_personas':numero_personas,'personas':personas})
def despedirse(args):
    return HttpResponse("Despedida desde django")
def contacto(request):
    return HttpResponse("Email:contactomail.com,Tel.555662322")