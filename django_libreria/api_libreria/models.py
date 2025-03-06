from django.db import models

# Create your models here.
class Autor(models.Model):
    id_autor = models.AutoField(primary_key=True, editable=False,db_column='T001IdAutor')
    nombre = models.CharField(max_length=100, db_column='T001Nombre')
    apellido = models.CharField(max_length=100, db_column='T001Apellido')
    biografia = models.CharField(max_length=200, db_column='T001Documento', blank=True, null=True) ##OPCIONAL 
    

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        db_table = 'T001'
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'