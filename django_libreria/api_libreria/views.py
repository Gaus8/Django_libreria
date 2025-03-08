from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.response import Response  # type: ignore
from rest_framework import generics, status  # type: ignore
from rest_framework.exceptions import NotFound, ValidationError # type: ignore
from .models import Autor,Editorial,Libro,Miembro,Prestamo
from .serializers import AutorSerializer,LibroSerializer,PrestamoSerializer
from django.db.models import Q

#Buscar libro por autor o editorial 
class BuscarLibro(generics.ListCreateAPIView):
    serializer_class = LibroSerializer  # Define el serializador a utilizar

    # Método GET para listar los libros
    def get_queryset(self):
        buscar = self.request.query_params.get('buscar', None) #Obtiene el parametro para buscar los libros
        if buscar: 
            libros = Libro.objects.filter( #Filtracion de los libros que coincidan 
                Q(autor__nombre__icontains=buscar) | Q(editorial__nombre__icontains=buscar)  #Busca los libros por los parametros indicados
            )
            return libros #Retorna el libro encontrado
        return Libro.objects.all()  #Imprimir todos los libros sin busqueda
    def get(self, request, *args, **kwargs):
            libros = self.get_queryset() #Obtiene la informacion de los libros de get_queryset
            if not libros.exists():
                 raise NotFound('No se encontraron libros.')  # Lanza una excepción si no se encuentran los libros

            serializer = self.get_serializer(libros,many=True)         
            return Response({'success': True, 'detail': 'Libros encontrados.', 'data': serializer.data}, status=status.HTTP_200_OK)  # Devuelve una respuesta con los datos serializados


#Consultar prestamos de libros
class ConsultarLibro(generics.ListCreateAPIView):
    serializer_class = PrestamoSerializer # Define el serializador a utilizar


    # Método GET para consultar los libros prestados
    def get_queryset1(self):
        buscar = self.request.query_params.get('buscar', None)  #Obtiene el parametro para buscar el libro
        if buscar:
            try:
                from datetime import datetime #Importacion de la libreria para la hora
                fecha_busqueda = datetime.strptime(buscar, "%y-%m-%d").date() #Capturar la fecha ingresada
                 
                librosP = Prestamo.objects.filter( #Filtra los libros encontrados
                     Q(fecha=fecha_busqueda ) | Q(miembro__nombre__icontains=buscar) #Busca los libros prestados por la hora o por el miembro
                )

            except ValueError:
                print("ERROR!! \nDatos invalidos. (Presiona un numero)") #En caso de diligenciar un dato no valido le registra un error

            return librosP
        return Prestamo.objects.all() #Muestra todos los prestamos 
    
    def get(self, request, *args, **kwargs):
            prestamos = self.get_queryset1() #Informacion arrojada por get_queryset1
            if not prestamos.exists():
                 raise NotFound('No se encontraron libros prestados.')  # Lanza una excepción si no se encuentran los libros

            serializer = self.get_serializer(prestamos,many=True)         
            return Response({'success': True, 'detail': 'Libros encontrados.', 'data': serializer.data}, status=status.HTTP_200_OK)  # Devuelve una respuesta con los datos serializados