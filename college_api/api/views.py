from api.models import College, Attribute
from api.serializers import CollegeSerializer, AttributeSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


class CollegeList(generics.ListCreateAPIView):
    """
    List all colleges, or create a new college.
    """
    queryset = College.objects.all()
    serializer_class = CollegeSerializer


class CollegeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a college instance.
    """
    queryset = College.objects.all()
    serializer_class = CollegeSerializer


class CollegeAttributeAdd(APIView):
    """
    Add a pre-existing attribute to a college.
    """
    def put(self, request, format=None, **kwargs):
        college = get_object_or_404(College, pk=kwargs['college_pk'])
        attribute_pk = request.data['pk']
        attribute = get_object_or_404(Attribute, pk=attribute_pk)
        college.attributes.add(attribute)
        college.save()
        return Response(status=status.HTTP_200_OK)
        

class AttributeList(generics.ListCreateAPIView):
    """
    List all attributes, or create a new attribute.
    """
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer


class AttributeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete an attribute instance.
    """
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer
