from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HeroSerializer, VillianSerializer
from .models import Hero, Villian



class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('id')
    serializer_class = HeroSerializer

class VillianViewSet(viewsets.ModelViewSet):
    queryset = Villian.objects.all().order_by('id')
    serializer_class = VillianSerializer
