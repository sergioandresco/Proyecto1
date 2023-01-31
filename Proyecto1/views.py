from django.http import HttpResponse;

def saludo(request): #primera vista
    
    return HttpResponse("Hola mundo, esta es la primera pagina con Django");