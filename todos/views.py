from django.shortcuts import render
from rest_framework import generics
from todos import serializers

from todos.models import Todo

# crear todos y editar
class TodosAPIView(generics.ListCreateAPIView):
    queryset=Todo.objects.all().order_by("-id")
    #traducir a json
    serializer_class= serializers.TodoSerializer 

#recuperar todo actualizarlo o eliminarlo
class TodoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Todo.objects.all()
    serializer_class=serializers.TodoSerializer   