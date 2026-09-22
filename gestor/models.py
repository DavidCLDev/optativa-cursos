from django.db import models

# Create your models here.
class Curso(models.Model):

    NIVEL_CHOICES = [
        ('PRINCIPIANTE', 'Principiante'),
        ('INTERMEDIO', 'Intermedio'),
        ('AVANZADO', 'Avanzado')
    ]

    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    nivel = models.CharField(
        max_length=12,
        choices=NIVEL_CHOICES,
        default='INTERMEDIO'
    )
    imagen = models.ImageField(upload_to="img/", default="img/logo.png")

    def __str__(self):
        return self.titulo

class Leccion(models.Model):

    ESTADO_CHOICES = [
        ('BORRADOR', 'Borrador'),
        ('PUBLICADO', 'Publicado')
    ]

    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    duracion = models.IntegerField()
    estado = models.CharField(
        max_length=9,
        choices=ESTADO_CHOICES,
        default='BORRADOR'
    )
    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
        related_name='lecciones'
    )

    def __str__(self):
        return self.titulo + " (" + self.curso.titulo + ")"