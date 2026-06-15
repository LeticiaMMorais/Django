from django.shortcuts import render

def menu_view(request):
    contexto = {
        'nome_loja':'Geek Burger',
        'loja_aberta': True,
        'promocao_do_dia':'Franburguer',
        'lanches':[
            {'nome':'Franburguer', 'preco':'10.00'},
            {'nome':'X-burguer', 'preco':'16.00'},
            {'nome':'Baconburguer', 'preco':'13.00'},
            {'nome':'Hambúrguer Vegano', 'preco':'20.00'},
            {'nome':'Batata Frita', 'preco':'10.00'},
            {'nome':'Espetinho', 'preco':'6.00'},
        ]
    }

    return render(request, 'cardapio/cardapio.html', contexto)
