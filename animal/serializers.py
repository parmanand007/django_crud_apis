from rest_framework import serializers
from .models import Animal
from django.contrib.auth.models import User


class AnimalSerializer(serializers.ModelSerializer):  # create class to serializer model
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Animal
        fields = ('id', 'name', 'type','sound','owner','extra_information','created_at','updated_at')


class UserSerializer(serializers.ModelSerializer):  # create class to serializer user model
    animals = serializers.PrimaryKeyRelatedField(many=True, queryset=Animal.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'animals')
