# Importa la función path del módulo de URLs de Django
from django.urls import path
# Importa las vistas desde el módulo views de la aplicación actual
from .views import (
    ConsultarLibro,BuscarLibro,CrearLibro, EliminarLibro, ActualizarLibro,
    ConsultarAutor, CrearAutor,EliminarAutor,ActualizarAutor,
    CrearEditorial,ConsultarEditorial,EliminarEditorial,ActualizarEditorial,
    CrearMiembro,CrearPrestamo
)

# Define la lista de patrones de URL para la aplicación 'api_app'
urlpatterns = [
    # Rutas para la gestión de libros
    # Lista de libros
    path('librerias/', BuscarLibro.as_view(), name='librerias-list'),
    path('prestamo/', ConsultarLibro.as_view(), name='libro-prestamo'),
    #CRUD AUTOR
    path('consultar/autor/',ConsultarAutor.as_view(), name='consultar_autores'),
    path('crear/autor/',CrearAutor.as_view(), name='crear_autores'),
    path('autor/<int:id_autor>/eliminar/',EliminarAutor.as_view(), name='eliminar_autores'),
    path('autor/<int:id_autor>/actualizar/',ActualizarAutor.as_view(), name='actulizar_autores'),
    #CRUD EDITORIAL
    path('consultar/editorial/',ConsultarEditorial.as_view(), name='consultar_editoriales'),
    path('crear/editorial/',CrearEditorial.as_view(), name='crear_editoriales'),
    path('ditorial/<int:id_editorial>/eliminar/',EliminarEditorial.as_view(), name='eliminar_editoriales'),
    path('editorial/<int:id_editorial>/actualizar/',ActualizarEditorial.as_view(), name='actualizar_Editoriales'),
    #CRUD LIBRO
    path('libro/', CrearLibro.as_view(), name='libros'),
    path('miembro/', CrearMiembro.as_view(), name='miembros'),
    path('prestamo/', CrearPrestamo.as_view(), name='prestamo')
    ]