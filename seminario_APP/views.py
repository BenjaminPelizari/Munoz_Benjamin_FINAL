from django.http import Http404, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Inscrito, Institucion
from .forms import InscritoForm, InstitucionForm
from .serializers import InscritoSerializer, InstitucionSerializer
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from rest_framework.views import APIView


class InscritoCrear(CreateView):
    model = Inscrito
    form_class = InscritoForm
    template_name = 'inscrito_form.html'
    success_url = reverse_lazy('inscrito_crear')

class InstitucionCrear(CreateView):
    model = Institucion
    form_class = InstitucionForm
    template_name = 'institucion_form.html'
    success_url = reverse_lazy('institucion_crear')

#CLASS para inscritos
class InscritoAPI(APIView):
    def get(self, request):
        inscritos = Inscrito.objects.all()
        serializer = InscritoSerializer(inscritos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InscritoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'Confirmado', 'message': 'Inscrito creado correctamente'}, status=status.HTTP_201_CREATED)
        return Response({'status': 'error', 'message': 'Error al crear el inscrito'}, status=status.HTTP_400_BAD_REQUEST)

class InscritoDetalles(APIView):
    def get(self, request, pk):
        inscrito = get_object_or_404(Inscrito, pk=pk)
        serializer = InscritoSerializer(inscrito)
        return Response(serializer.data)

    def put(self, request, pk):
        inscrito = get_object_or_404(Inscrito, pk=pk)
        serializer = InscritoSerializer(inscrito, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'Confirmado', 'message': 'Inscrito actualizado correctamente'})
        return Response({'status': 'error', 'message': 'Error al actualizar el inscrito'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        inscrito = get_object_or_404(Inscrito, pk=pk)
        inscrito.delete()
        return Response({'status': 'Eliminado con exito', 'message': 'Inscrito eliminado correctamente'})
    

#Fuctions para el institucion

@api_view(['GET', 'POST'])
def InstitucionAPI(request):
    if request.method == 'GET':
        instituciones = Institucion.objects.all()
        serializer = InstitucionSerializer(instituciones, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = InstitucionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'Confirmado', 'message': 'Institución creada correctamente'}, status=status.HTTP_201_CREATED)
        return Response({'status': 'error', 'message': 'Error al crear la institución'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def institucionDetalles(request, pk):
    institucion = get_object_or_404(Institucion, pk=pk)

    if request.method == 'GET':
        serializer = InstitucionSerializer(institucion)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = InstitucionSerializer(institucion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'Confirmado', 'message': 'Institución actualizada correctamente'})
        return Response({'status': 'Error', 'message': 'Error al actualizar la institución'}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        institucion.delete()
        return Response({'status': 'Confirmado', 'message': 'Institución eliminada correctamente'})

def DatosUsuario(request):
    usuario = {
        'id': 1,
        'Nombre': 'Benjamin',
        'Apellidos': 'Muñoz Pelizari',
        'Carrera': 'Ingenieria Informatica',
        'edad': '20',
    }
    return JsonResponse(usuario)

def index(request):
    return render(request, 'index.html')
