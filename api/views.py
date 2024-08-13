from django.shortcuts import render
from django.http import JsonResponse
from .serializers import BlogInfoSerializer
from .models import BlogInfo
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['GET', 'POST'])
def blog_list(request, format=None):

    if request.method == 'GET':
        blogs = BlogInfo.objects.all()
        serializer = BlogInfoSerializer(blogs, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = BlogInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

@api_view(['GET', 'PUT', 'DELETE'])
def blog_detail(request, id, format=None):
    
    try:
        blog = BlogInfo.objects.get(pk=id)
    except BlogInfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = BlogInfoSerializer(blog)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = BlogInfoSerializer(blog, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)