from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from gestor.models import Curso, Leccion

@login_required
def listar_cursos(request):
    '''
    Obtiene todos los cursos registrados en la base de datos para
    renderizarlos en la plantilla lista-cursos.html
    '''
    cursos = Curso.objects.all()

    return render(request, "lista-cursos.html", {"cursos": cursos})

@login_required
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
        # Título del curso
        titulo = request.POST.get("titulo")
        # Descripción del curso
        descripcion = request.POST.get("descripcion")
        # Nivel del curso (PRINCIPIANTE, INTERMEDIO o AVANZADO)
        nivel = request.POST.get("nivel")
        # Imagen del curso
        imagen = request.FILES.get("imagen")

        if titulo and descripcion and nivel:
            # Se verifica que se recibieron correctamente los datos requeridos
            
            # Creación del curso con sus respectivos atributos
            curso = Curso(titulo=titulo, nivel=nivel, descripcion=descripcion)

            if imagen:
                # Se valida que se recibió la imagen del curso antes de asignarla
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

@login_required
def detallar_curso(request, id_curso):
    curso = get_object_or_404(Curso, id=id_curso)

    return render(request, "detalle-curso.html", {"curso": curso})

@login_required
def editar_curso(request, id_curso):
    # Se obtiene el curso son el ID indicado por parámetro, si no lo encuentra
    # lanza un código de estado 404 (Not Found)
    curso = get_object_or_404(Curso, id=id_curso)

    if request.method == 'POST':
        # Título del curso
        titulo = request.POST.get("titulo")
        # Descripción del curso
        descripcion = request.POST.get("descripcion")
        # Nivel del curso (PRINCIPIANTE, INTERMEDIO o AVANZADO)
        nivel = request.POST.get("nivel")
        # Imagen del curso
        imagen = request.FILES.get("imagen")

        if titulo and descripcion and nivel:
            # Se verifica que se recibieron correctamente los datos requeridos

            # Se modifica cada uno de los atributos antiguos por los valores
            # recibidos.
            curso.titulo = titulo
            curso.descripcion = descripcion
            curso.nivel = nivel

            if imagen:
                # Se valida que se recibió la imagen del curso antes de
                # asignarla.
                curso.imagen = imagen

            # Se guarda el curso modificado en el modelo.
            curso.save()
        
        return redirect("detalle_curso", id_curso)

    return render(request, "editar-curso.html", {"curso": curso})

@login_required
def eliminar_curso(request, id_curso: int) -> HttpResponse:
    curso = Curso.objects.get(pk=id_curso)

    curso.delete()

    return redirect("lista_cursos")

@login_required
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

@login_required
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
    
    return render(
        request,
        "editar-leccion.html",
        {
            "leccion": leccion
        }
    )

@login_required
@require_POST
def eliminar_leccion(request, id):
    leccion = get_object_or_404(Leccion, id=id)
    id_curso = leccion.curso.id

    leccion.delete()

    return redirect('detalle_curso', id_curso)