from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
def registrar(request):
    datos = ''
    errors = []

    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        datos = request.POST

        if User.objects.filter(email=email).exists():
            errors.append('El correo electrónico ya está registrado')
        
        if User.objects.filter(username=username).exists():
            errors.append('El nombre de usuario ya está en uso')
        
        if password1 != password2:
            errors.append('Las contraseñas no coinciden')
        
        if not errors:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password1,
                first_name=first_name,
                last_name=last_name
            )

            login(request, user)
            return redirect('/')

    return render(request, 'registro.html', {'errors':errors, 'datos':datos})