from django.db import models

# Create your models here.
class Autor (models.Model):
    id_autor = models.AutoField(primary_key=True, editable=False,db_column='T001IdAutor')
    nombre = models.CharField(max_length=100, db_column='T001Nombre')
    apellido = models.CharField(max_length=100, db_column='T001Apellido')
    biografia = models.TextField(db_column='T001Biografia', blank=True, null=True) #OPCIONAL 
    

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        db_table = 'T001'
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

class Editorial (models.Model):
    id_editorial = models.AutoField(primary_key=True, editable=False,db_column='T002IdEditorial')
    nombre = models.CharField(max_length=100, db_column='T002Nombre')
    direccion = models.CharField(max_length=80, db_column='T002Direccion')
    telefono = models.CharField(max_length=20, db_column='T002Telefono', blank=True, null=True) #OPCIONAL 
    

    def __str__(self):
        return f"{self.nombre} {self.direccion}"

    class Meta:
        db_table = 'T002'
        verbose_name = 'Editorial'
        verbose_name_plural = 'Editoriales'

class Libro (models.Model):
    id_Libro = models.AutoField(primary_key=True, editable=False, db_column='T003IdLibro')
    titulo = models.CharField(max_length=100, db_column='T003Titulo')
    resumen = models.TextField(db_column='T003Resumen')
    isbn = models.CharField(max_length=20, unique=True, db_column='T003ISBN')
    fecha_publicacion = models.DateField(db_column='T003Fecha_Publicacion' )
    ##RELACIONES Foreign Key
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE,related_name='libros', db_column='T001IdAutor')
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE,related_name='libros', db_column='T002IdEditorial')

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = 'T003'
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'