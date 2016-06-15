from api.models import College, Attribute, User
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
    Add a pre-existing attribute to a college. Returns 404 if attribute
    does not exist.
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


class UserCollegeListModifyRetrieve(generics.ListAPIView):
    """
    Retrieve and modify a user's college list.
    """
    serializer_class = CollegeSerializer

    def get_queryset(self):
        user_id = self.kwargs['pk']
        user = get_object_or_404(User, pk=user_id)
        queryset = user.colleges
        return queryset

    def put(self, request, format=None, **kwargs):
        user_id = self.kwargs['pk']
        user = get_object_or_404(User, pk=user_id)
        college_pk = request.data['pk']
        college = get_object_or_404(College, pk=college_pk)
        user.colleges.add(college)
        user.save()
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, format=None, **kwargs):
        user_id = self.kwargs['pk']
        user = get_object_or_404(User, pk=user_id)
        college_pk = request.data['pk']
        college = get_object_or_404(user.colleges, pk=college_pk)
        user.colleges.remove(college)
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
