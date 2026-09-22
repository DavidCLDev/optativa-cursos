from django.urls import path, include
from . import views

urlpatterns = [
    # lista de cursos
    path(
        '',
        views.listar_cursos,
        name="lista_cursos"
    ),
    # Creación curso
    path(
        'curso/nuevo/',
        views.crear_curso,
        name="crear_curso"
    ),
    # Detalle curso
    path(
        'curso/<int:id_curso>/',
        views.detallar_curso,
        name="detalle_curso"
    ),
    # Edición curso
    path(
        'curso/<int:id_curso>/editar/',
        views.editar_curso,
        name="editar_curso"
    ),
    # Eliminación curso
    path(
        'curso/<int:id_curso>/eliminar/',
        views.eliminar_curso,
        name="eliminar_curso"
    ),
    # Creación Lección
    path(
        'curso/<int:id_curso>/lecciones/crear/',
        views.crear_leccion,
        name="crear_leccion"
    ),
    # Edición Lección
    path(
        'lecciones/<int:id>/editar',
        views.editar_leccion,
        name="editar_leccion"
    ),
    # Eliminación Lección
    path(
        'lecciones/<int:id>/eliminar',
        views.eliminar_leccion,
        name="eliminar_leccion"
    ),
]