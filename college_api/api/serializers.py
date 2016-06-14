from rest_framework import serializers
from api.models import Attribute, College


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ('id', 'name', 'category')


class CollegeSerializer(serializers.ModelSerializer):
    attributes = AttributeSerializer(many=True)

    class Meta:
        model = College
        fields = ('id', 'name', 'size', 'attributes')

    def create(self, validated_data):
        attributes_data = validated_data.pop('attributes')
        college = College.objects.create(**validated_data)
        for attribute_data in attributes_data:
            Attribute.objects.create(college=college, **attribute_data)
        return college

    def update(self, validated_data):
        attributes_data = validated_data.pop('attributes')
        college = College.objects.update(**validated_data)
        for attribute_data in attributes_data:
            Attribute.objects.update(college=college, **attribute_data)
        return college
