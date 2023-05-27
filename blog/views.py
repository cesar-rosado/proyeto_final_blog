from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from blog.models import Categoria, Articulo
# Create your views here.

####VISTAS POR CLASE PARA MODELO CATEGORIA
class CategoriaListView(ListView):
    model = Categoria
    template_name = 'blog/categorias.html'

class CategoriaCreateView(CreateView):
    model = Categoria
    fields = ('nombre',)
    success_url = reverse_lazy('categorias')

class CategoriaDetailView(DetailView):
    model = Categoria
    success_url = reverse_lazy('categorias')

class CategoriaUpdateView(UpdateView):
    model = Categoria
    fields = ('nombre',)
    success_url = reverse_lazy('categorias')

class CategoriaDeleteView(DeleteView):
    model = Categoria
    success_url = reverse_lazy('categorias')


### VISTAS POR CLASE PARA MODELO ARTICULO

class ArticuloListView(ListView):
    model = Articulo
    template_name = 'blog/articulos.html'

class ArticuloCreateView(CreateView):
    model = Articulo
    fields = ('titulo', 'categoria', 'fecha', 'contenido', 'autor', 'imagen')
    success_url = reverse_lazy('articulos')
    
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class ArticuloDetailView(DetailView):
    model = Articulo
    success_url = reverse_lazy('articulo')

class ArticuloUpdateView(UpdateView):
    model = Articulo
    fields = ('titulo', 'categoria', 'fecha', 'contenido', 'autor', 'imagen')
    success_url = reverse_lazy('articulos')
    
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class ArticuloDeleteView(DeleteView):
    model = Articulo
    success_url = reverse_lazy('articulos')