from django.shortcuts import render
from rest_framework import generics
from .models import Event
from . import serializers

# Create your views here.
class EventsList(generics.ListAPIView):
    """Представление списка новостей (только для чтения)"""

    queryset = Event.objects.all()
    serializer_class = serializers.EventsListSerializer
