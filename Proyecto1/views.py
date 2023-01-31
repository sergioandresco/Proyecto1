from django.http import HttpResponse;

#Creamos vistas para poder utilizarlas

def saludo(request): #primera vista
    
    return HttpResponse("Hola mundo, esta es la primera pagina con Django");

def suma(request):
    
    x = 2;
    y = 2;
    
    suma = x + y;
    
    return HttpResponse(suma);