from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.generics import ListAPIView

from drf.serializers import PassSerializer
from main.models import Pass


class PassViewSet(viewsets.ModelViewSet):
    queryset = Pass.objects.all()
    serializer_class = PassSerializer

