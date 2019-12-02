from django.shortcuts import render

# Create your views here.
def user_add(request):
    return render (request, 'users/users_index.html', {'message':'prueba desde views'})