from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product, Categoria


def home(request):
    produtos_destaque = Product.objects.filter(destaque=True)  # Filtra apenas os produtos marcados como destaque
    produtos_promocao = Product.objects.filter(promocao=True)  # Filtra apenas os produtos em promoção
    
    context = {
        'products': produtos_destaque,
        'produtos_promocao': produtos_promocao,
    }
    return render(request, 'index.html', context)


def sobre(request):
    return render(request, 'pages/sobre.html')  # Caminho correto para sobre.html


def contato(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        endereco = request.POST.get('endereco', '')
        email = request.POST.get('email')
        mensagem = request.POST.get('mensagem')

        # Criar a mensagem do e-mail
        assunto = f"Novo Contato de {nome}"
        corpo_email = f"""
        Nome: {nome}
        Telefone: {telefone}
        Endereço: {endereco}
        E-mail: {email}
        Mensagem: {mensagem}
        """

        destinatario = "luam10@hotmail.com.br"  # Altere para o e-mail que receberá as mensagens

        email_envio = EmailMessage(
            assunto,
            corpo_email,
            to=[destinatario],
            reply_to=[email]  # Permite que você responda diretamente ao e-mail do cliente
        )

        try:
            email_envio.send()
            messages.success(request, "Sua mensagem foi enviada com sucesso!")
        except Exception as e:
            messages.error(request, "Ocorreu um erro ao enviar a mensagem. Tente novamente.")

        return redirect('contact')  # Redireciona para a página de contato

    return render(request, 'pages/contact.html')


def lista_produtos(request):
    query = request.GET.get('q', '').strip()  # Captura e remove espaços extras
    categorias = Categoria.objects.all()
    produtos_por_categoria = {}

    if query:
        produtos = Product.objects.filter(title__icontains=query) | Product.objects.filter(categoria__name__icontains=query)
    else:
        produtos = Product.objects.all()

    for categoria in categorias:
        produtos_categoria = produtos.filter(categoria=categoria)
        if produtos_categoria.exists():
            produtos_por_categoria[categoria.name] = produtos_categoria

    return render(request, 'pages/produtos.html', {
        'produtos_por_categoria': produtos_por_categoria,
        'query': query  # Passa a pesquisa para o template
    })
