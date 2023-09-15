from django.urls import path
from todos import views


urlpatterns = [
    path("todos/", views.TodosAPIView.as_view()),
    path("todo/<int:pk>/" , views.TodoAPIView.as_view()),
    #agrego id pk(entero) django primarkey=id y NO CONFUNFIR CON VIEWS:TODOS!
]
