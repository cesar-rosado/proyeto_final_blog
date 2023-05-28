from django.shortcuts import render, redirect
from django.urls import reverse
from usuarios.forms import RegisterForm
# Create your views here.

def registro(request):
    if request.method == "POST":
        formulario = RegisterForm(request.POST)

        if formulario.is_valid():
            formulario.save()  
            url_exitosa = reverse('inicio')
            return redirect(url_exitosa)
    else: 
        formulario = RegisterForm()
    
    return render(
        request=request,
        template_name='usuarios/registro.html',
        context={'form': formulario},
    )
