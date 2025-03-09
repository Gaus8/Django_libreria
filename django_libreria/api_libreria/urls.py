# Importa la función path del módulo de URLs de Django
from django.urls import path
# Importa las vistas desde el módulo views de la aplicación actual
from .views import (
    ConsultarLibro,BuscarLibro,CrearLibro, EliminarLibro, ActualizarLibro,
    ConsultarAutor, CrearAutor,EliminarAutor,ActualizarAutor,
    CrearEditorial,ConsultarEditorial,EliminarEditorial,ActualizarEditorial,
    CrearMiembro,ConsultarMiembro,EliminarMiembro, ActualizarMiembro,
    CrearPrestamo
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
    path('editorial/',ConsultarEditorial.as_view(), name='consultar_editoriales'),
    path('editorial/',CrearEditorial.as_view(), name='crear_editoriales'),
    path('editorial/<int:id_editorial>/eliminar/',EliminarEditorial.as_view(), name='eliminar_editoriales'),
    path('editorial/<int:id_editorial>/actualizar/',ActualizarEditorial.as_view(), name='actualizar_editoriales'),
    #CRUD LIBRO
    path('librerias/', BuscarLibro.as_view(), name='librerias-list'),
    path('libro/', ConsultarLibro.as_view(), name='consultar_libros'),
    path('libro/', CrearLibro.as_view(), name='crear_libros'),
    path('libro/<int:id_libro>/eliminar/',EliminarLibro.as_view(), name='eliminar_libros'),
    path('libro/<int:id_libro>/actualizar/',ActualizarLibro.as_view(), name='actualizar_libros'),
    #CRUD MIEMBRO
    path('miembro/', ConsultarMiembro.as_view(), name='consultar_miembros'),
    path('miembro/', CrearMiembro.as_view(), name='crear_miembros'),
    path('miembro/<int:id_miembro>/eliminar/',EliminarMiembro.as_view(), name='eliminar_miembros'),
    path('miembro/<int:id_miembro>/actualizar/',ActualizarMiembro.as_view(), name='actualizar_miembros'),
    #CRUD PRESTAMO
    path('prestamo/', CrearPrestamo.as_view(), name='prestamo')
    ]