# Importa la función path del módulo de URLs de Django
from django.urls import path
# Importa las vistas desde el módulo views de la aplicación actual
from .views import (
    ConsultarLibro,FiltrarLibro,CrearLibro, EliminarLibro, ActualizarLibro,
    ConsultarAutor, CrearAutor,EliminarAutor,ActualizarAutor,
    CrearEditorial,ConsultarEditorial,EliminarEditorial,ActualizarEditorial,
    CrearMiembro,ConsultarMiembro,EliminarMiembro, ActualizarMiembro,
    ConsultarPrestamos,CrearPrestamos,FiltrarPrestamos,EliminarPrestamos,ActualizarPrestamos
)

# Define la lista de patrones de URL para la aplicación 'api_app'
urlpatterns = [
    #CRUD AUTOR
    path('autor/',ConsultarAutor.as_view(), name='consultar_autores'),
    path('autor/',CrearAutor.as_view(), name='crear_autores'),
    path('autor/<int:id_autor>/',EliminarAutor.as_view(), name='eliminar_autores'),
    path('autor/<int:id_autor>/',ActualizarAutor.as_view(), name='actulizar_autores'),
    #CRUD EDITORIAL
    path('editorial/',ConsultarEditorial.as_view(), name='consultar_editoriales'),
    path('editorial/',CrearEditorial.as_view(), name='crear_editoriales'),
    path('editorial/<int:id_editorial>/',EliminarEditorial.as_view(), name='eliminar_editoriales'),
    path('editorial/<int:id_editorial>/',ActualizarEditorial.as_view(), name='actualizar_editoriales'),
    #CRUD LIBRO
    path('librerias/', FiltrarLibro.as_view(), name='filtrar_libros'),
    path('libro/', ConsultarLibro.as_view(), name='consultar_libros'),
    path('libro/', CrearLibro.as_view(), name='crear_libros'),
    path('libro/<int:id_libro>/',EliminarLibro.as_view(), name='eliminar_libros'),
    path('libro/<int:id_libro>/',ActualizarLibro.as_view(), name='actualizar_libros'),
    #CRUD MIEMBRO
    path('miembro/', ConsultarMiembro.as_view(), name='consultar_miembros'),
    path('miembro/', CrearMiembro.as_view(), name='crear_miembros'),
    path('miembro/<int:id_miembro>/',EliminarMiembro.as_view(), name='eliminar_miembros'),
    path('miembro/<int:id_miembro>/',ActualizarMiembro.as_view(), name='actualizar_miembros'),
    #CRUD PRESTAMO
    path('prestamo/', ConsultarPrestamos.as_view(), name='consultar_prestamos'),
    path('prestamo/', FiltrarPrestamos.as_view(), name='filtrar_prestamos'),
    path('prestamo/', CrearPrestamos.as_view(), name='crear_prestamos'),
    path('prestamo/<int:id_prestamo>/eliminar/',EliminarPrestamos.as_view(), name='eliminar_prestamos'),
    path('prestamo/<int:id_prestamo>/actualizar/',ActualizarMiembro.as_view(), name='actualizar_prestamos'),
    ]