from django.urls import path
from .views import home, sobre, contato, lista_produtos

urlpatterns = [
    path('', home, name='home'),
    path('pages/sobre/', sobre, name='sobre'),
    path('pages/contact/', contato, name='contact'),
    path('pages/produtos/', lista_produtos, name='produtos'),
]
