from django.db import models

class Nivel(models.TextChoices):
    PRINCIPIANTE = 'PRINCIPIANTE', 'Principiante'
    INTERMEDIO = 'INTERMEDIO', 'Intermedio'
    AVANZADO = 'AVANZADO', 'Avanzado'

# Create your models here.
class Curso(models.Model):

    titulo = models.CharField()
    nivel = models.CharField(
        max_length=12,
        choices=Nivel.choices,
        default=Nivel.PRINCIPIANTE
    )
    num_lecciones = models.DecimalField(max_digits=2, decimal_places=0)