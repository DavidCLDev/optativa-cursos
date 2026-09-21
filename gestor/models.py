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
    num_lecciones = models.DecimalField(max_digits=2, decimal_places=0)

    def __str__(self):
        return self.titulo