from django.db import models

class Categoria(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')

    class Meta:
       ordering = ['name']
       verbose_name = 'Categoria'

    def __str__(self):
        return self.name
    
  

class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='Produtos')
    descricao = models.TextField(null=True, verbose_name='Descrição')
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço')
    destaque = models.BooleanField(default=False, verbose_name='Destaque')
    promocao = models.BooleanField(default=False, verbose_name='Promoção')
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True, verbose_name='Imagem Produto')  # Campo de imagem

    class Meta:
       ordering = ['title']
       verbose_name = 'Produto'

    def __str__(self):
        return self.title
