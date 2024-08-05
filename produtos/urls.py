from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listar/', views.listar, name='listar'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('alterar/<int:id>', views.alterar, name='alterar'),
    path('excluir/<int:id>', views.excluir, name='excluir'),
]
