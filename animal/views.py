from django.shortcuts import render

# Create your views here.



from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from .models import Animal
from .permissions import IsOwnerOrReadOnly
from .serializers import AnimalSerializer
from .pagination import CustomPagination
from .filters import AnimalFilter

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def animal_list_create_view(request):
    if request.method == 'GET':
        animals = Animal.objects.all()

        # Apply filtering if query parameters are present
        animal_filter = AnimalFilter(request.GET, queryset=animals)
        animals = animal_filter.qs

        # Apply pagination
        pagination = CustomPagination()
        paginated_animals = pagination.paginate_queryset(animals, request)

        serializer = AnimalSerializer(paginated_animals, many=True)
        return pagination.get_paginated_response(serializer.data)

    elif request.method == 'POST':
        serializer = AnimalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated, IsOwnerOrReadOnly])
def animal_detail_view(request, pk):
    try:
        animal = Animal.objects.get(pk=pk)
    except Animal.DoesNotExist:
        response={"status":"not found"}
        return Response(response,status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AnimalSerializer(animal)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AnimalSerializer(animal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # #we can add validation for super user
        # print("delete")
        animal.delete()
        response={"status":"deleted succesfully","entity":animal.name}
        return Response(response,status=status.HTTP_204_NO_CONTENT)
