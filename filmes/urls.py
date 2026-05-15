from django.urls import path
from . import views

app_name = 'filmes'

urlpatterns = [
    path('', views.listaFilmes, name='listaFilmes'),
    path('detalhe/', views.detalheFilme, name='detalheFilme'),
]
