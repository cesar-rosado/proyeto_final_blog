from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from django.views.generic import UpdateView

from usuarios.forms import RegisterForm, UpdateForm, AvatarForm
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

def login_view(request):
    next_url = request.GET.get('next')
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data
            usuario = data.get('username')
            password = data.get('password')
            user = authenticate(username=usuario, password=password)
            # user puede ser un usuario o None
            if user:
                login(request=request, user=user)
                if next_url:
                    return redirect(next_url)
                url_exitosa = reverse('inicio')
                return redirect(url_exitosa)
    else:  # GET
        form = AuthenticationForm()
    return render(
        request=request,
        template_name='usuarios/login.html',
        context={'form': form},
    )

class CustomLogoutView(LogoutView):
   template_name = 'usuarios/logout.html'
   
class MiPerfilUpdateView(LoginRequiredMixin, UpdateView):
   form_class = UpdateForm
   success_url = reverse_lazy('inicio')
   template_name = 'usuarios/formulario_usuario.html'

   def get_object(self, queryset=None):
       return self.request.user

def agregar_avatar(request):
  if request.method == "POST":
      formulario = AvatarForm(request.POST, request.FILES) # Aquí me llega toda la info del formulario html

      if formulario.is_valid():
          avatar = formulario.save()
          avatar.user = request.user
          avatar.save()
          url_exitosa = reverse('inicio')
          return redirect(url_exitosa)
  else:  # GET
      formulario = AvatarForm()
      
  return render(
      request=request,
      template_name="usuarios/avatar.html",
      context={'form': formulario},
  )