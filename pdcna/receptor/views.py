from django.shortcuts import render

from django.forms.models import model_to_dict

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework import status

from .parsers import JSONParser
from .models import Participante, Levantamento, Levantamento_dados
from .serializers import ParticipanteSerializer, LevantamentoSerializer, Levantamento_dadosSerializer
import json

# Create your views here.
def index(request):
	return render(request, 'dash/index.html')

class ParticipanteView(APIView):
	parser_classes = (JSONParser,)
	def put(self, request):
		data = ParticipanteSerializer(data=json.loads(request.data))
		if data.is_valid():
			post_data = data.validated_data
			Participante.objects.create(**post_data)
			return Response({"resposta":'ok'})
		else:
			return Response({"resposta":data.errors}, status=status.HTTP_400_BAD_REQUEST)

	def get(self, request):
		lista = [model_to_dict(p) for p in Participante.objects.all()]
		return Response({"resposta":lista})

class LevantamentoView(APIView):
	parser_classes = (JSONParser,)
	def put(self, request):
		data = LevantamentoSerializer(data=json.loads(request.data))
		if data.is_valid():
			post_data = data.validated_data
			Levantamento.objects.create(**post_data)
			return Response({"resposta":'ok'})
		else:
			return Response({"resposta":data.errors}, status=status.HTTP_400_BAD_REQUEST)

	def get(self, request):
		lista = [model_to_dict(p) for p in Levantamento.objects.all()]
		return Response({"resposta":lista})

class Levantamento_dadosView(APIView):
	parser_classes = (JSONParser,)
	def put(self, request):
		data = Levantamento_dadosSerializer(data=json.loads(request.data))
		if data.is_valid():
			post_data = data.validated_data
			Levantamento_dados.objects.create(**post_data)
			return Response({"resposta":'ok'})
		else:
			return Response({"resposta":data.errors}, status=status.HTTP_400_BAD_REQUEST)

	def get(self, request):
		lista = [model_to_dict(p) for p in Levantamento_dados.objects.all()]
		return Response({"resposta":lista})