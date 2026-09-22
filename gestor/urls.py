from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.listar_cursos, name="lista_cursos"),
    path('curso/nuevo/', views.crear_curso, name="crear_curso"),
    path('curso/<int:id_curso>/', views.detallar_curso, name="detalle_curso"),
    path('curso/<int:id_curso>/editar/', views.editar_curso, name="editar_curso"),
    path('curso/<int:id_curso>/eliminar/', views.eliminar_curso, name="eliminar_curso"),
    path('curso/<int:id_curso>/lecciones/crear/', views.crear_leccion, name="crear_leccion"),
    path('lecciones/<int:id>/eliminar', views.eliminar_leccion, name="eliminar_leccion")
]