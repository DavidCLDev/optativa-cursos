from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from gestor.models import Curso, Leccion

# Create your views here.
def listar_cursos(request):
    '''
    Obtiene todos los cursos registrados en la base de datos para
    renderizarlos en la plantilla lista-cursos.html
    '''
    cursos = Curso.objects.all()

    return render(request, "lista-cursos.html", {"cursos": cursos})

def crear_curso(request):
    '''
    Gestiona la creación de un nuevo curso.

    Si la solicitud utiliza el método POST, obtiene los datos del formulario
    (título, descripción, nivel e imagen), valida que los campos obligatorios
    estén presentes y crea un nuevo objeto Curso en la base de datos.

    Args:
        request (HttpRequest): Solicitud HTTP enviada por el cliente.

    Returns:
        HttpResponse:
            - Redirección a la lista de cursos después de procesar una
              solicitud POST.
            - Renderizado de "nuevo-curso.html" para solicitudes que no sean
              POST.
    '''
    if request.method == 'POST':
        titulo = request.POST.get("titulo")
        descripcion = request.POST.get("descripcion")
        nivel = request.POST.get("nivel")
        imagen = request.FILES.get("imagen")

        if titulo and descripcion and nivel:
            curso = Curso(titulo=titulo, nivel=nivel, descripcion=descripcion)
            if imagen:
                curso.imagen = imagen
            curso.save()
        
        return redirect("lista_cursos")
    
    return render(
        request,
        "nuevo-curso.html",
        {
            "nivel_choices": Curso.NIVEL_CHOICES
        }
    )

def detallar_curso(request, id_curso):
    curso = get_object_or_404(Curso, id=id_curso)

    return render(request, "detalle-curso.html", {"curso": curso})

def editar_curso(request, id_curso):
    curso = get_object_or_404(Curso, id=id_curso)

    if request.method == 'POST':
        titulo = request.POST.get("titulo")
        descripcion = request.POST.get("descripcion")
        nivel = request.POST.get("nivel")
        imagen = request.FILES.get("imagen")

        print(imagen)

        if titulo and descripcion and nivel:
            curso.titulo = titulo
            curso.descripcion = descripcion
            curso.nivel = nivel
            if imagen:
                curso.imagen = imagen

            curso.save()
        
        return redirect("detalle_curso", id_curso)

    return render(request, "editar-curso.html", {"curso": curso})

def eliminar_curso(request, id_curso: int) -> HttpResponse:
    curso = Curso.objects.get(pk=id_curso)

    curso.delete()

    return redirect("lista_cursos")

def crear_leccion(request, id_curso):
    curso = get_object_or_404(Curso, id=id_curso)

    if request.method == 'POST':
        titulo = request.POST.get("titulo")
        contenido = request.POST.get("contenido")
        estado = request.POST.get("estado")
        duracion = request.POST.get("duracion")

        if titulo and contenido and estado and duracion:
            leccion = Leccion(
                titulo=titulo,
                estado=estado,
                contenido=contenido,
                duracion=duracion,
                curso=curso
            )
            leccion.save()
        
        return redirect("detalle_curso", id_curso)
    
    return render(
        request,
        "nueva-leccion.html",
        {
            "estado_choices": Leccion.ESTADO_CHOICES,
            "id_curso": id_curso
        }
    )

def editar_leccion(request, id):
    leccion = get_object_or_404(Leccion, id=id)

    if request.method == 'POST':
        titulo = request.POST.get("titulo")
        contenido = request.POST.get("contenido")
        estado = request.POST.get("estado")
        duracion = request.POST.get("duracion")

        if titulo and contenido and estado and duracion:
            leccion.titulo = titulo
            leccion.contenido = contenido
            leccion.estado = estado
            leccion.duracion = duracion

            leccion.save()
        
        return redirect("detalle_curso", leccion.curso.id)

    print(leccion.titulo)
    
    return render(
        request,
        "editar-leccion.html",
        {
            "leccion": leccion
        }
    )

@require_POST
def eliminar_leccion(request, id):
    leccion = get_object_or_404(Leccion, id=id)
    id_curso = leccion.curso.id

    leccion.delete()

    return redirect('detalle_curso', id_curso)