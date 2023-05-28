from django.contrib import admin
from django.urls import path

from usuarios.views import registro, login_view, CustomLogoutView, agregar_avatar, MiPerfilUpdateView

urlpatterns = [
    path('registro/', registro, name="registro"),
    path('login/', login_view, name="login"),
    path('logout/', CustomLogoutView.as_view(), name="logout"),
    path('avatar/', agregar_avatar, name="agregar_avatar"),
    path('editar-usuario/', MiPerfilUpdateView.as_view(), name="editar_perfil"),
]