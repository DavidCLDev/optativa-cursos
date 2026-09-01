from django.shortcuts import render, redirect
from django.http import HttpResponse
from gestor.models import Curso

# Create your views here.
def lista_cursos(request):
    cursos = Curso.objects.all()

    return render(request, "lista_cursos.html", {"cursos": cursos})

def crear_curso(request):
    if request.method == 'POST':
        print("hola")
        titulo = request.POST.get("titulo")
        nivel = request.POST.get("nivel")
        num_lecciones = request.POST.get("num_lecciones")

        if titulo and nivel and num_lecciones:
            curso = Curso(titulo=titulo, nivel=nivel, num_lecciones=num_lecciones)
            curso.save()
        
        return redirect("lista_cursos")
    
    return render(request, "creacion_curso.html")

    

def detalle_curso(request, id_curso):
    curso = Curso.objects.get(pk=id_curso)

    return render(request, "detalle_curso.html", {"curso": curso})

def eliminar_curso(request, id_curso: int) -> HttpResponse:
    curso = Curso.objects.get(pk=id_curso)

    curso.delete()

    return redirect("lista_cursos")

def edicion_curso(request, id_curso):
    return HttpResponse(f"edtar curso: {id_curso}")

def test(request):
    return render(request, "test.html")