import re
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Propietario, Edificio, Departamento
from .serializers import PropietarioSerializer, EdificioSerializer, DepartamentoSerializer


# Create your views here.


def index(request):
    return JsonResponse({'mensaje': 'Bienvenido a mi api'})

@api_view(['GET','post'])
def propietarios(request):
    if request.method == 'GET':
        lstPropietarios = Propietario.objects.all()
        serPropietarios = PropietarioSerializer(lstPropietarios,many=True)
        return Response(serPropietarios.data)
    elif request.method == 'POST':
        print(request.data)
        serPropietarios = PropietarioSerializer(data=request.data)
        if serPropietarios.is_valid():
            serPropietarios.save()
            return Response(serPropietarios.data)
        else:
            return Response(serPropietarios.errores)

    
@api_view(['GET','POST'])
def edificios(request):
    if request.method == 'GET':
        lstEdificios = Edificio.objects.all()
        serEdificios = EdificioSerializer(lstEdificios, many=True)
        return Response(serEdificios.data)
    elif request.method == 'POST':
        serEdificios = EdificioSerializer(data=request.data)
        if serEdificios.is_valid():
            serEdificios.save()
            return Response(serEdificios.data)
        else:
            return Response(serEdificios.errors)

@api_view(['GET','POST'])
def departamentos(request):
    if request.method == 'GET': 
        lstDepartamentos = Departamento.objects.all()
        serDepartamentos = DepartamentoSerializer(lstDepartamentos,many=True)
        return Response(serDepartamentos.data)
    elif request.method == 'POST':
        serDepartamentos = DepartamentoSerializer(data=request.data)
        if serDepartamentos.is_valid():
            serDepartamentos.save()
            return Response(serDepartamentos.data)
        else:
            return Response(serDepartamentos.errors) 

@api_view(['GET','PUT','DELETE'])
def propietario(request,propietario_id):
    objPropietario = Propietario.objects.get(id=propietario_id)

    if request.method == 'GET':
        serPropietario = PropietarioSerializer(objPropietario)
        return Response(serPropietario.data)
    elif request.method == 'PUT':
        serPropietario = PropietarioSerializer(objPropietario,data=request.data)
        if serPropietario.is_valid():
            serPropietario.save()
            return Response(serPropietario.data)
        else:
            return Response(serPropietario.errors,status=400) 
    elif request.method == 'DELETE':
        objPropietario.delete()
        return Response(status=204)

# def create(self, validated_data):
#     departamento = validated_data.pop('departamentos')
#     edificio = Edificio.objects.create(**validated_data)
#     for departamento_data in departamento_data:
#         Departamento.objects.create(edificio=edificio, **edificio_data)
#     return edificio