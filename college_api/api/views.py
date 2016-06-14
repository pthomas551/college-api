from django.shortcuts import render
from api.models import College, Attribute
from api.serializers import CollegeSerializer, AttributeSerializer
from rest_framework import generics


class CollegeList(generics.ListCreateAPIView):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer


class CollegeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer


class AttributeList(generics.ListCreateAPIView):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer


class AttributeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer
