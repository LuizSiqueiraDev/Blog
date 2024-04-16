"""Define padrões de URL para aprendizado_app."""
from django.urls import path
from . import views

app_name = 'aprendizado_app'
urlpatterns = [
    #Página Inicial
    path('', views.index, name='index'),
]
