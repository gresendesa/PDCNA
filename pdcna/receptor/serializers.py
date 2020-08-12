from rest_framework import serializers
from .models import Participante, Levantamento, Levantamento_dados
#from .validators import MaxInt, MinInt

class ParticipanteSerializer(serializers.Serializer):
    nome = serializers.CharField(required=True, max_length=100)
    data_nascimento = serializers.DateField(required=True)

class LevantamentoSerializer(serializers.Serializer):
    data = serializers.DateField(required=True)
    participante = serializers.PrimaryKeyRelatedField(queryset=Participante.objects.all())

class Levantamento_dadosSerializer(serializers.Serializer):
	levantamento = serializers.PrimaryKeyRelatedField(queryset=Levantamento.objects.all())
	variavel = serializers.CharField(required=True, max_length=45)
	valor = serializers.DecimalField(max_digits=10, decimal_places=0)