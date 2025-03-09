from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.response import Response  # type: ignore
from rest_framework import generics, status  # type: ignore
from rest_framework.exceptions import NotFound, ValidationError # type: ignore
from .models import Autor,Editorial,Libro,Miembro,Prestamo
from .serializers import AutorSerializer,LibroSerializer,PrestamoSerializer, EditorialSerializer, MiembroSerializer
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
    
    #Metodo POST para añadir Autor, editorial, Libro, Miembro, Prestamo 


#AUTOR
# GET
class ConsultarAutor(generics.ListCreateAPIView):
    queryset = Autor.objects.all()  # Define el conjunto de consultas para obtener todos los autores
    serializer_class = AutorSerializer  # Define el serializador a utilizar

    # Método GET para listar todos los autores
    def get(self, request):
        autores = Autor.objects.all()  # Obtiene todas los autores
        serializer = AutorSerializer(autores, many=True)  # Serializa los autores
        if not autores:
            raise NotFound('No se encontraron personas.')  # Lanza una excepción si no se encuentran autores
        return Response({'success': True, 'detail': 'Listado de personas.', 'data': serializer.data}, status=status.HTTP_200_OK)  # Devuelve una respuesta con los datos serializados

# POST
class CrearAutor(generics.CreateAPIView):
    queryset = Autor.objects.all()  # Define el conjunto de consultas para obtener todos los autores
    serializer_class = AutorSerializer  # Define el serializador a utilizar

    # Método POST para crear una nueva autor
    def post(self, request):
        serializer = AutorSerializer(data=request.data)  # Serializa los datos de la solicitud
        serializer.is_valid(raise_exception=True)  # Valida los datos y lanza una excepción si no son válidos
        serializer.save()  # Guarda la nueva persona
        return Response({'success': True, 'detail': 'Autor creado correctamente.', 'data': serializer.data}, status=status.HTTP_201_CREATED)  # Devuelve una respuesta con los datos de la nueva persona

# DELETE
class EliminarAutor(generics.DestroyAPIView): # USO DE DESTROY PARA ELIMINAR DATOS
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    lookup_field = 'fk'#USO DEL ID DE LA TABLA PARA LA ELIMINACION

#PUT
class ActualizarAutor(generics.UpdateAPIView): #USO DE UPDATE PARA ACTUALIZAR DATOS
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    lookup_field = 'id_autor'  #USO DEL ID DE LA TABLA PARA LA MODIFICACION

##EDITORIAL

#GET
class ConsultarEditorial(generics.ListCreateAPIView):
    queryset = Editorial.objects.all()  # Define el conjunto de consultas para obtener todas las editoriales
    serializer_class = EditorialSerializer  # Define el serializador a utilizar

    # Método GET para listar todas las editoriales
    def get(self, request):
        editoriales = Editorial.objects.all()  # Obtiene todas las editoriales
        serializer = AutorSerializer(editoriales, many=True)  # Serializa las editoriales
        if not editoriales:
            raise NotFound('No se encontraron editoriales')  # Lanza una excepción si no se encuentran las editorirales
        return Response({'success': True, 'detail': 'Listado de Editoriales', 'data': serializer.data}, status=status.HTTP_200_OK)  # Devuelve una respuesta con los datos serializados

#POST
    # Vista específica para crear una editorial
class CrearEditorial(generics.CreateAPIView):
    queryset = Editorial.objects.all()  # Define el conjunto de consultas para obtener todas las editoriales
    serializer_class = Editorial  # Define el serializador a utilizar

    # Método POST para crear una nueva editorial
    def post(self, request):
        serializer = EditorialSerializer(data=request.data)  # Serializa los datos de la solicitud
        serializer.is_valid(raise_exception=True)  # Valida los datos y lanza una excepción si no son válidos
        serializer.save()  # Guarda la nueva editorial
        return Response({'success': True, 'detail': 'Persona creada correctamente.', 'data': serializer.data}, status=status.HTTP_201_CREATED)  # Devuelve una respuesta con los datos de la nueva editorial
    
#DELETE 
class EliminarEditorial(generics.DestroyAPIView): # USO DE DESTROY PARA ELIMINAR DATOS
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer
    lookup_field = 'id_editorial'#USO DEL ID DE LA TABLA PARA LA ELIMINACION

#PUT
class ActualizarEditorial(generics.UpdateAPIView): #USO DE UPDATE PARA ACTUALIZAR DATOS
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer
    lookup_field = 'id_editorial'  #USO DEL ID DE LA TABLA PARA LA MODIFICACION

#LIBRO
#FILTRAR
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

#GET
class ConsultarLibro(generics.ListCreateAPIView):
    queryset = Libro.objects.all()  # Define el conjunto de consultas para obtener todos los libro
    serializer_class = LibroSerializer  # Define el serializador a utilizar

    # Método GET para listar todas las personas
    def get(self, request):
        libros = Libro.objects.all()  # Obtiene todas los libros
        serializer = LibroSerializer(libros, many=True)  # Serializa los libros
        if not libros:
            raise NotFound('No se encontraron libros registrados')  # Lanza una excepción si no se encuentran libros
        return Response({'success': True, 'detail': 'Listado de Editoriales', 'data': serializer.data}, status=status.HTTP_200_OK)  # Devuelve una respuesta con los datos serializados

#POST
    # Vista específica para crear un libro
class CrearLibro(generics.CreateAPIView):
    queryset = Libro.objects.all()  # Define el conjunto de consultas para obtener todas libros
    serializer_class = LibroSerializer  # Define el serializador a utilizar

    # Método POST para crear un nuevo libro 
    def post(self, request):
        serializer = LibroSerializer(data=request.data)  # Serializa los datos de la solicitud
        serializer.is_valid(raise_exception=True)  # Valida los datos y lanza una excepción si no son válidos
        serializer.save()  # Guarda el nuevo libro
        return Response({'success': True, 'detail': 'Persona creada correctamente.', 'data': serializer.data}, status=status.HTTP_201_CREATED)  # Devuelve una respuesta con los datos del nuevo libro

#DELETE 
class EliminarLibro(generics.DestroyAPIView): # USO DE DESTROY PARA ELIMINAR DATOS
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    lookup_field = 'id_libro'#USO DEL ID DE LA TABLA PARA LA ELIMINACION

#PUT
class ActualizarLibro(generics.UpdateAPIView): #USO DE UPDATE PARA ACTUALIZAR DATOS
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    lookup_field = 'id_libro'  #USO DEL ID DE LA TABLA PARA LA MODIFICACION

## MIEMBRO

#GET
class ConsultarMiembro(generics.ListCreateAPIView):
    queryset =  Miembro.objects.all()  # Define el conjunto de consultas para obtener todos los miembros
    serializer_class = MiembroSerializer  # Define el serializador a utilizar

    # Método GET para listar todas las personas
    def get(self, request):
        miembros = Miembro.objects.all()  # Obtiene todas los libros
        serializer = MiembroSerializer(miembros, many=True)  # Serializa las personas
        if not miembros:
            raise NotFound('No se encontraron miembros registrados')  # Lanza una excepción si no se encuentran personas
        return Response({'success': True, 'detail': 'Listado de Editoriales', 'data': serializer.data}, status=status.HTTP_200_OK)  # Devuelve una respuesta con los datos serializados

#POST
    # Vista específica para crear miembros
class CrearMiembro(generics.CreateAPIView):
    queryset = Miembro.objects.all()  # Define el conjunto de consultas para obtener todas las personas
    serializer_class = MiembroSerializer  # Define el serializador a utilizar

    # Método POST para crear un nuevo miembro
    def post(self, request):
        serializer = MiembroSerializer(data=request.data)  # Serializa los datos de la solicitud
        serializer.is_valid(raise_exception=True)  # Valida los datos y lanza una excepción si no son válidos
        serializer.save()  # Guarda el nuevo miembro
        return Response({'success': True, 'detail': 'Persona creada correctamente.', 'data': serializer.data}, status=status.HTTP_201_CREATED)  # Devuelve una respuesta con los datos del nuevo miembro
    
#DELETE 
class EliminarMiembro(generics.DestroyAPIView): # USO DE DESTROY PARA ELIMINAR DATOS
    queryset = Miembro.objects.all()
    serializer_class = MiembroSerializer
    lookup_field = 'id_miembro'#USO DEL ID DE LA TABLA PARA LA ELIMINACION

#PUT
class ActualizarMiembro(generics.UpdateAPIView): #USO DE UPDATE PARA ACTUALIZAR DATOS
    queryset = Miembro.objects.all()
    serializer_class = MiembroSerializer
    lookup_field = 'id_miembro'  #USO DEL ID DE LA TABLA PARA LA MODIFICACION




    # Vista específica para crear prestamo
class CrearPrestamo(generics.CreateAPIView):
    queryset = Prestamo.objects.all()  # Define el conjunto de consultas para obtener todas las personas
    serializer_class = PrestamoSerializer  # Define el serializador a utilizar

    # Método POST para crear un nuevo prestamo
    def post(self, request):
        serializer =PrestamoSerializer(data=request.data)  # Serializa los datos de la solicitud
        serializer.is_valid(raise_exception=True)  # Valida los datos y lanza una excepción si no son válidos
        serializer.save()  # Guarda el nuevo prestamo
        return Response({'success': True, 'detail': 'Persona creada correctamente.', 'data': serializer.data}, status=status.HTTP_201_CREATED)  # Devuelve una respuesta con los datos del nuevo prestamo