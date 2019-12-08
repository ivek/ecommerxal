from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
# Create your views here.


def user_add(request):
    return render(request, 'users/users_index.html', {'message': 'prueba desde views'})


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(user)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('users_add')

        else:
            messages.error(request, 'Usuario o contraseña no valido')

    return render(request, 'users/login.html')
