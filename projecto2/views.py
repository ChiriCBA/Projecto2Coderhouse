from time import time
from django.http import HttpResponse
import datetime
from django.template import Template, Context
def saludo(request):   #Nuestra primera vista :) 
	return HttpResponse("Hola Django - Coder")


def segunda_vista(request):
    return HttpResponse("<br><br>Ya entendimos esto, es muy simple :) ")

def diaDeHoy(request):

        dia = datetime.datetime.now()

        documentoDeTexto = f"Hoy es día: <br> {dia}"


        return HttpResponse(documentoDeTexto)


def miNombreEs(self, nombre):

    

      documentoDeTexto = f"Mi nombre es: <br><br>  {nombre}"

def anionacimiento (Self, edad):
    yearnow = datetime.datetime.now().year
    yearbirth = yearnow - int(edad)
    documentodetexto2 = f"tu año de nacimiento es: {yearbirth}"
    return HttpResponse(documentodetexto2)




def probandoTemplate(self):

    miHtml = open("E:/Coderhouse/Class_17_django/projecto2/projecto2/templates/template.html")

    plantilla = Template(miHtml.read()) #Se carga en memoria nuestro documento, template1   
    ##OJO importar template y contex, con: from django.template import Template, Context

    miHtml.close() #Cerramos el archivo

    miContexto = Context() #EN este caso no hay nada ya que no hay parametros, IGUAL hay que crearlo

    documento = plantilla.render(miContexto) #Aca renderizamos la plantilla en documento

    return HttpResponse(documento)