from rest_framework import serializers
from .models import Departamento, Edificio, Propietario


class PropietarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propietario
        fields = '__all__'


class DepartamentoSerializer(serializers.ModelSerializer):
    propietario = serializers.PrimaryKeyRelatedField(many=False, queryset=Propietario.objects.all())
    edificio = serializers.PrimaryKeyRelatedField(many=False, queryset=Edificio.objects.all())

    class Meta:
        model = Departamento
        fields = ['numero', 'propietario', 'edificio']


class EdificioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Edificio
        fields = ['nombre']

