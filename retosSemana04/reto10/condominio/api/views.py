from django.http import JsonResponse

from .models import Propietario, Edificio, Departamento

# Create your views here.


def index(request):
    return JsonResponse({'mensaje': 'Bienvenido a mi api'})

def propietarios(request):
    lstPropietarios = Propietario.objects.all()
    print(lstPropietarios)
    data = []
    for propietario in lstPropietarios:
        data.append({
            'nombre': propietario.nombre,
            'dni': propietario.dni,
            'telefono': propietario.telefono,
            'email': propietario.email

        })
    return JsonResponse(data, safe=False)

def edificios(request):
    lstEdificios = Edificio.objects.all()
    print(lstEdificios)
    data = []
    for edificio in lstEdificios:
        data.append({
            'nombre': edificio.nombre,

        })
    return JsonResponse(data, safe=False)

def departamentos(request):
    lstDepartamentos = Departamento.objects.all()
    print(lstDepartamentos)
    data = []
    for departamento in lstDepartamentos:
        data.append({
            'numero': departamento.numero,

        })
    return JsonResponse(data, safe=False)
