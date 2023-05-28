from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from blog.models import Categoria, Articulo
from proyecto_blog  import settings
# Create your views here.

####VISTAS POR CLASE PARA MODELO CATEGORIA
class CategoriaListView(LoginRequiredMixin, ListView):
    model = Categoria
    template_name = 'blog/categorias.html'

class CategoriaCreateView(LoginRequiredMixin, CreateView):
    model = Categoria
    fields = ('nombre',)
    success_url = reverse_lazy('categorias')

class CategoriaDetailView(LoginRequiredMixin, DetailView):
    model = Categoria
    success_url = reverse_lazy('categorias')

class CategoriaUpdateView(LoginRequiredMixin, UpdateView):
    model = Categoria
    fields = ('nombre',)
    success_url = reverse_lazy('categorias')

class CategoriaDeleteView(LoginRequiredMixin, DeleteView):
    model = Categoria
    success_url = reverse_lazy('categorias')


### VISTAS POR CLASE PARA MODELO ARTICULO

class ArticuloListView(ListView):
    model = Articulo
    template_name = 'blog/articulos.html'

class ArticuloCreateView(LoginRequiredMixin, CreateView):
    model = Articulo
    fields = ('titulo', 'categoria', 'fecha', 'contenido', 'autor', 'imagen')
    success_url = reverse_lazy('articulos')
    
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ruta_imagen'] = settings.MEDIA_URL + 'img_articulos/'
        return context

class ArticuloDetailView(DetailView):
    model = Articulo
    success_url = reverse_lazy('articulo')

class ArticuloUpdateView(LoginRequiredMixin, UpdateView):
    model = Articulo
    fields = ('titulo', 'categoria', 'fecha', 'contenido', 'autor', 'imagen')
    success_url = reverse_lazy('articulos')
    
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ruta_imagen'] = settings.MEDIA_URL + 'img_articulos/'
        return context

class ArticuloDeleteView(LoginRequiredMixin, DeleteView):
    model = Articulo
    success_url = reverse_lazy('articulos')
