# Importa la función path del módulo de URLs de Django
from django.urls import path
# Importa las vistas desde el módulo views de la aplicación actual
from .views import (
    ConsultarLibro,BuscarLibro, CrearAutor,CrearEditorial,CrearLibro,CrearMiembro,CrearPrestamo
)

# Define la lista de patrones de URL para la aplicación 'api_app'
urlpatterns = [
    # Rutas para la gestión de libros
    # Lista de libros
    path('librerias/', BuscarLibro.as_view(), name='librerias-list'),
    path('consultar/prestamo/', ConsultarLibro.as_view(), name='libro-prestamo'),
    path('crear/autor/',CrearAutor.as_view(), name='autores'),
    path('crear/editorial/',CrearEditorial.as_view(), name='Editoriales'),
    path('crear/libro/', CrearLibro.as_view(), name='libros'),
    path('crear/miembro/', CrearMiembro.as_view(), name='miembros'),
    path('crear/prestamo/', CrearPrestamo.as_view(), name='prestamo')
    ]