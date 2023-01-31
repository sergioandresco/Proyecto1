from django.http import HttpResponse;
import datetime;
from django.template import Template, Context;

#Creamos vistas para poder utilizarlas

def saludo(request): #primera vista
    
    doc_externo = open("E:/ProyectosDjango/Proyecto1/Proyecto1/Plantillas/Index.html");
    
    plantilla = Template(doc_externo.read());
    
    doc_externo.close();
    
    contexto = Context();
    
    documento = plantilla.render(contexto);
    
    return HttpResponse(documento);

def suma(request):
    
    x = 2;
    y = 2;
    
    suma = x + y;
    
    return HttpResponse(suma);

def date(request):
    
    fecha_actual = datetime.datetime.now();
    
    return HttpResponse(fecha_actual);

def calcula_edad(request, edad, anio):
    
    edad_actual = edad;
    periodo = anio - 2023;
    edad_futura = edad_actual + periodo;
    documento = """
    <html>
    <body>
        <center><h1>
            En el año %s tendrás %s años
        </h1></center>
    </body>
    </html>
    """ %(anio, edad_futura);
    
    return HttpResponse(documento);