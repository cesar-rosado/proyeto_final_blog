from django.contrib import admin
from django.urls import path

from blog.views import CategoriaCreateView, CategoriaDeleteView, CategoriaDetailView, CategoriaListView, CategoriaUpdateView, \
    ArticuloCreateView, ArticuloDetailView, ArticuloListView, ArticuloUpdateView, ArticuloDeleteView

urlpatterns = [
    # URLS DE CATEGORIA
    path("categorias/", CategoriaListView.as_view(), name="categorias"),
    path('categorias/<int:pk>/', CategoriaDetailView.as_view(), name="ver_categoria"),
    path('crear-categoria/', CategoriaCreateView.as_view(), name="crear_categoria"),
    path('editar-categoria/<int:pk>/', CategoriaUpdateView.as_view(), name="editar_categoria"),
    path('eliminar-categoria/<int:pk>/', CategoriaDeleteView.as_view(), name="eliminar_categoria"),
    
    # URLS DE ARTICULOS
    path("articulos/", ArticuloListView.as_view(), name="articulos"),
    path('articulo/<int:pk>/', ArticuloDetailView.as_view(), name="ver_articulo"),
    path('crear-articulo/', ArticuloCreateView.as_view(), name="crear_articulo"),
    path('editar-articulo/<int:pk>/', ArticuloUpdateView.as_view(), name="editar_articulo"),
    path('eliminar-articulo/<int:pk>/', ArticuloDeleteView.as_view(), name="eliminar_articulo"),
]