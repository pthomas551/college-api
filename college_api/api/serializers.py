from rest_framework import serializers
from api.models import Attribute, College, User


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ('id', 'name', 'category')


class CollegeSerializer(serializers.ModelSerializer):
    attributes = AttributeSerializer(many=True)

    class Meta:
        model = College
        fields = ('id', 'name', 'size', 'attributes')


class UserSerializer(serializers.ModelSerializer):
    colleges = CollegeSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'name')
