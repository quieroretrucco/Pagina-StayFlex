from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from APP3.models import Departamento,Propietario,Huesped,Estadia
from APP3.forms import DepartamentoFormulario,PropietarioFormulario,HuespedFormulario,EstadiaFormulario

def departamento(self):
  departamento = Departamento()
  departamento.save() 

def propietario(self):
  propietario = Propietario()
  propietario.save()   

def huesped(self):
  huesped = Huesped()
  huesped.save()

def estadia(self):
  estadia = Estadia()
  estadia.save()    

def inicio(request):
    return render(request,"APP3/index.html")


#def departamento(request):
 #   return render(request, 'APP3/departamento.html') #no anda


def propietario(request):
    return HttpResponse('vista propietarios')


#def huesped(request):
 #   return render(request, 'APP3/huesped.html')


def estadia(request):
    return HttpResponse('vista estadia')


def departamentoFormulario(request):
      if request.method == "POST":
            miFormulario = DepartamentoFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  departamento = Departamento(barrio=informacion["barrio"], piso=informacion["piso"],depto=informacion["depto"])
                  departamento.save()
                  return render(request, "APP3/index.html")
      else:
            miFormulario = DepartamentoFormulario()
      return render(request, "APP3/departamento_formulario.html", {"miFormulario": miFormulario})

def propietarioFormulario(request):
      if request.method == "POST":
            miFormulario = PropietarioFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  propietario= Propietario(nombre=informacion["nombre"], apellido=informacion["apellido"],email=informacion["email"])
                  propietario.save()
                  return render(request, "APP3/index.html")
      else:
            miFormulario = PropietarioFormulario()
      return render(request, "APP3/propietario_formulario.html", {"miFormulario": miFormulario})

def huespedFormulario(request):
      if request.method == "POST":
            miFormulario = HuespedFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  huesped= Huesped(nombre=informacion["nombre"], apellido=informacion["apellido"],email=informacion["email"],nacionalidad=informacion["nacionalidad"])
                  huesped.save()
                  return render(request, "APP3/index.html")
      else:
            miFormulario = HuespedFormulario()
      return render(request, "APP3/huesped_formulario.html", {"miFormulario": miFormulario})

def estadiaFormulario(request):
      if request.method == "POST":
            miFormulario = EstadiaFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  estadia= Estadia(check_in=informacion["check_in"], check_out=informacion["check_out"])
                  estadia.save()
                  return render(request, "APP3/index.html")
      else:
            miFormulario = EstadiaFormulario()
      return render(request, "APP3/estadia_formulario.html", {"miFormulario": miFormulario})

def buscar_barrio(request):
    return render(request, 'APP3/buscar_barrio.html')
#def buscar(request):
    #barrio = request.GET.get('barrio', '')
    #if barrio:
        # Perform your search logic here
     #   response = f'Buscando resultados para {barrio}'
     #   return HttpResponse(response)
    #else:
     #   respuesta = 'No barrio provided.'
      #  return HttpResponse(respuesta)

def buscar(request):
      if request.GET['barrio']:
        barrio = request.GET['barrio']
        departamento = Departamento.objects.filter(barrio__icontains=barrio)
        return render(request, 'APP3/resultados_busqueda.html', {'barrio': barrio, 'departamento': departamento})
      else:
        respuesta = 'No enviaste datos.'
        return HttpResponse(respuesta)