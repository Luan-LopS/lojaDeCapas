from django.contrib import admin
from .models import Categoria, Product

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    search_fields= ('name',)
    list_filter=('is_active',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'categoria', 'descricao','preco','destaque','promocao','imagem')
    search_fields= ('title', 'categoria', 'descricao')
    list_filter=('title',)