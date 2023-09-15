from django.db import models


# Create your models here.
class Todo(models.Model):
    title= models.CharField(max_length=100)
    #restringe tamaño y valida datos ingresados
    done=models.BooleanField(default=False)
    #almacenar fecha
    created=models.DateTimeField(auto_now_add=True)
