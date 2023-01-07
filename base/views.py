from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .photos import photos

# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/photos/',
        '/api/photos/add/',

        '/api/photos/upload/',

        '/api/photos/<id>/',
        '/api/photos/<id>/comments/',

        '/api/user/<id>/',
        '/api/user/<id>/photos',
    ]
    return Response(routes)

@api_view(['GET'])
def getPhotos(request):
    return Response(photos)

@api_view(['GET'])
def getPhoto(request, pk):
    product = None
    for i in photos:
        if i['id'] == pk:
            photo = i
            break
        
    return Response(photo)