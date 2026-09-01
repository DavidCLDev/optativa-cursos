from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.lista_cursos, name="lista_cursos"),
    path('curso/nuevo/', views.crear_curso, name="crear_curso"),
    path('curso/<int:id_curso>/', views.detalle_curso, name="detalle_curso"),
    path('curso/<int:id_curso>/editar/', views.edicion_curso),
    path('curso/<int:id_curso>/eliminar/', views.eliminar_curso, name="eliminar_curso"),
    path('test', views.test)
]