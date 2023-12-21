"""
URL configuration for Munoz_Benjamin_FINAL project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from seminario_APP import views

urlpatterns = [
    path('', views.index, name='index'),

    # Inscrito
    path('inscrito_crear/', views.InscritoCrear.as_view(), name='inscrito_crear'),
    path('api_inscrito/', views.InscritoAPI.as_view()),
    path('api_inscrito/<int:pk>/', views.InscritoDetalles.as_view()),

    # Institucion 
    path('api_institucion/', views.InstitucionAPI),
    path('api_institucion/<int:pk>/', views.institucionDetalles),
    path('institucion_crear/', views.InstitucionCrear.as_view(), name='institucion_crear'),
    #Datos pal user
    path('usuario/', views.DatosUsuario),
]
