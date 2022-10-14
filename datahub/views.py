import json
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import authentication, permissions
from .models import *
from .serializers import * 

# Create your views here.
class MatchViewSet(ModelViewSet):
    queryset = MatchDB.objects.all()
    serializer_class = MatchSerializer

    def create(self, request, *args, **kwargs):
        kwargs['many'] = isinstance(request.data, json)
        serializer = self.get_serializer(data=request.data, **kwargs)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def partial_update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        if kwargs.pop("matchtype", None):
            serializer = self.get_serializer(
        	    instance=self.get_object(), data=request.data, **kwargs
	        )
        else:
            kwargs["many"] = isinstance(request.data, json)
            serializer = self.get_serializer(
    	        self.get_queryset(), data=request.data, **kwargs
	        )
        serializer.is_valid(raise_exception=True)




"""
10/14 ~ 16 
view에서 bulk(batch) CRUD 구현해서 matadata 넣을 예정.
"""