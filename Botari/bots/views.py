from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Bot, Scenario, Step
from .serializers import BotSerializer, ScenarioSerializer, StepSerializer
import openai

# Установите ваш API ключ OpenAI
OPENAI_API_KEY='sk-test-key-1234567890'
 # Замените на свой ключ

class BotViewSet(viewsets.ModelViewSet):
    queryset = Bot.objects.all()
    serializer_class = BotSerializer

# Вы можете добавить больше методов для работы с GPT API здесь, если нужно.

class ScenarioViewSet(viewsets.ModelViewSet):
    queryset = Scenario.objects.all()
    serializer_class = ScenarioSerializer

class StepViewSet(viewsets.ModelViewSet):
    queryset = Step.objects.all()
    serializer_class = StepSerializer