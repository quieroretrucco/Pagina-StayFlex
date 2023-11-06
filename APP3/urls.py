from django.urls import path
from APP3 import views
from django.shortcuts import render


urlpatterns = [
    path('', views.inicio),
    path('departamentoformulario/', views.departamentoFormulario, name="DepartamentoFormulario"),
    path('propietarioformulario/', views.propietarioFormulario, name="PropietarioFormulario"),
    path('huespedformulario/', views.huespedFormulario, name="HuespedFormulario"),
    path('estadiaformulario/', views.estadiaFormulario, name="EstadiaFormulario"),
    path('buscarBarrio/', views.buscar_barrio, name="BuscarBarrio"),
    path('buscarBarrio/buscar/', views.buscar),
    ]
