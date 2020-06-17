from django.shortcuts import render
from django.http import HttpResponse

def saludo(request): #Primera vista
    return HttpResponse("hola que mas")

def salida(request):
    return HttpResponse("bey gays")

def html(request):
    documento="""<html>
    <body>
    <h1>ahorasi</h1>
    <body>
    </html>
    """
    
    return HttpResponse(documento)
