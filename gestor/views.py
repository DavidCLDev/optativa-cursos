from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from gestor.models import Curso

# Create your views here.
def listar_cursos(request):
    cursos = Curso.objects.all()

    return render(request, "lista-cursos.html", {"cursos": cursos})

def crear_curso(request):
    if request.method == 'POST':
        titulo = request.POST.get("titulo")
        descripcion = request.POST.get("descripcion")
        nivel = request.POST.get("nivel")
        num_lecciones = request.POST.get("num_lecciones")

        if titulo and nivel and num_lecciones:
            curso = Curso(titulo=titulo, nivel=nivel, num_lecciones=num_lecciones, descripcion=descripcion)
            curso.save()
        
        return redirect("lista_cursos")
    
    return render(request, "creacion-curso.html", {"nivel_choices": Curso.NIVEL_CHOICES})

def detallar_curso(request, id_curso):
    curso = get_object_or_404(Curso, id=id_curso)

    return render(request, "detalle-curso.html", {"curso": curso})

def eliminar_curso(request, id_curso: int) -> HttpResponse:
    curso = Curso.objects.get(pk=id_curso)

    curso.delete()

    return redirect("lista_cursos")

def editar_curso(request, id_curso):
    curso = get_object_or_404(Curso, id=id_curso)

    return render(request, "editar-curso.html", {"curso": curso})