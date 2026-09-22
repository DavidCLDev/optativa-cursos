from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from gestor.models import Curso, Leccion

# Create your views here.
def listar_cursos(request):
    cursos = Curso.objects.all()

    return render(request, "lista-cursos.html", {"cursos": cursos})

def crear_curso(request):
    if request.method == 'POST':
        titulo = request.POST.get("titulo")
        descripcion = request.POST.get("descripcion")
        nivel = request.POST.get("nivel")

        if titulo and descripcion and nivel:
            curso = Curso(titulo=titulo, nivel=nivel, descripcion=descripcion)
            curso.save()
        
        return redirect("lista_cursos")
    
    return render(request, "nuevo-curso.html", {"nivel_choices": Curso.NIVEL_CHOICES})

def detallar_curso(request, id_curso):
    curso = get_object_or_404(Curso, id=id_curso)

    return render(request, "detalle-curso.html", {"curso": curso})

def eliminar_curso(request, id_curso: int) -> HttpResponse:
    curso = Curso.objects.get(pk=id_curso)

    curso.delete()

    return redirect("lista_cursos")

def editar_curso(request, id_curso):
    curso = get_object_or_404(Curso, id=id_curso)

    if request.method == 'POST':
        titulo = request.POST.get("titulo")
        descripcion = request.POST.get("descripcion")
        nivel = request.POST.get("nivel")

        if titulo and descripcion and nivel:
            curso.titulo = titulo
            curso.descripcion = descripcion
            curso.nivel = nivel
            curso.save()
        
        return redirect("detalle_curso", id_curso)

    return render(request, "editar-curso.html", {"curso": curso})

def crear_leccion(request, id_curso):
    curso = get_object_or_404(Curso, id=id_curso)

    if request.method == 'POST':
        titulo = request.POST.get("titulo")
        contenido = request.POST.get("contenido")
        estado = request.POST.get("estado")
        duracion = request.POST.get("duracion")

        if titulo and contenido and estado and duracion:
            leccion = Leccion(titulo=titulo, estado=estado, contenido=contenido, duracion=duracion, curso=curso)
            leccion.save()
        
        return redirect("detalle_curso", id_curso)
    
    return render(request, "nueva-leccion.html", {"estado_choices": Leccion.ESTADO_CHOICES, "id_curso": id_curso})

@require_POST
def eliminar_leccion(request, id):
    leccion = get_object_or_404(Leccion, id=id)
    id_curso = leccion.curso.id

    leccion.delete()

    return redirect('detalle_curso', id_curso)