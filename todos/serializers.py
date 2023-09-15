from rest_framework import serializers

from todos.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        #modelo a serializar
        model= Todo
        #campos a serializar
        fields="__all__"

