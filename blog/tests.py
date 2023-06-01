from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Categoria, Articulo
from datetime import datetime

# Create your tests here.
###TEST PARA CATEGORIA
class CategoriaTest(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(nombre='Categoria de prueba')

    def test_categoria_list(self):
        url = reverse('categorias')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.categoria.nombre)
        self.assertTemplateUsed(response, 'blog/categorias.html')

    def test_categoria_create(self):
        url = reverse('crear_categoria')
        response = self.client.post(url, {'nombre': 'Categoria de prueba'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Categoria.objects.last().nombre, 'Categoria de prueba')

    def test_categoria_detail(self):
        url = reverse('ver_categoria', args=[self.categoria.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.categoria.nombre)
        self.assertTemplateUsed(response, 'blog/categoria_detail.html')
    
    def test_categoria_update(self):
        url = reverse('editar_categoria', kwargs={'pk': self.categoria.pk})
        response = self.client.post(url, {'nombre': 'Categoria de prueba'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.categoria.nombre, 'Categoria de prueba')
        
    #def test_categoria_delete(self):
    #    url = reverse('eliminar_categoria', kwargs={'pk': self.categoria.pk})
    #    response = self.client.delete(url)
    #    self.assertEqual(response.status_code, 302)
    #    self.assertFalse(Categoria.objects.filter(pk=self.categoria.pk).exists())
        
###TEST PARA CLASE ARTICULO
    
class ArticuloTest(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(nombre='Categoria de prueba')
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.articulo = Articulo.objects.create(
            titulo='Articulo de prueba',
            categoria=self.categoria,
            fecha=datetime.now(),
            contenido='Contenido del articulo de prueba',
            autor=self.user
        )
    
    def test_articulo_detail_view(self):
        url = reverse('ver_articulo', args=[self.articulo.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.articulo.titulo)
        self.assertTemplateUsed(response, 'blog/articulo_detail.html')
        
    #def test_articulo_update_view(self):
    #    url = reverse('editar_articulo', kwargs={'pk': self.articulo.pk})
    #    articulo = Articulo.objects.get(pk=self.articulo.pk)
    #    response = self.client.post(url, {
    #        'titulo': 'Articulo de prueba actualizado',
    #        'contenido': 'Nuevo contenido',
    #        'imagen': '',
    #    })
    #    self.assertEqual(response.status_code, 302)
    #    self.articulo.refresh_from_db()
    #    print('Artículo antes de la actualización:', self.articulo.titulo)
    #    self.assertEqual(self.articulo.titulo, 'Articulo de prueba actualizado')
    #    print('Artículo después de la actualización:', self.articulo.titulo)
    #    self.assertEqual(self.articulo.contenido, 'Nuevo contenido')
    
    #def test_articulo_delete_view(self):
    #    url = reverse('eliminar_articulo', args=[self.articulo.pk])
    #    response = self.client.delete(url)
    #    self.assertEqual(response.status_code, 302)
    #    self.assertFalse(Articulo.objects.filter(pk=self.articulo.pk).exists())