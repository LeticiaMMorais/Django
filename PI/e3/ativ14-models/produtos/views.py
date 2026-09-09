from django.shortcuts import render
from . import models
from .forms import CriarProdutoForm

def retunProdutos():
    produtos = [
        {'id': 1, 
         'nome': 'Fone sem fio',
         'lote': '001',
         'categoria': 'Eletrônicos',
         'quantidade': 3
         },
        {'id': 2, 
         'nome': 'Vestido mid',
         'lote': '002',
         'categoria': 'Vestiário',
         'quantidade': 6
         },
        {'id': 3, 
         'nome': 'Base Dior',
         'lote': '003',
         'categoria': 'Cosméticos',
         'quantidade': 2
         },
        {'id': 4, 
         'nome': 'Máquina de lavar roupa',
         'lote': '004',
         'categoria': 'Eletrodoméstico',
         'quantidade': 8
         },
        {'id': 5, 
         'nome': 'Cif multiuso',
         'lote': '005',
         'categoria': 'Limpeza',
         'quantidade': 19
         }
    ]
    return produtos

# Create your views here.
def listagem(request):
    produtos = models.Produto.objects.all()
    context = {'produtos': produtos}
    return render(request, 'produtos/listagem.html', context)

def detalhes(request, id):
    produtos = models.Produto.objects.all()
    for item in produtos:
        if item.id == id:
            context = {
                'item': item
                }
    return render(request, 'produtos/detalhes.html', context)

def criar_produto(request):
    if request.method == "POST": 
        form = CriarProdutoForm(request.POST)
        if form.is_valid(): 
        # o .is_valid() faz todo o processo de validação. Por exemplo, verifica se um e-mail inserido está no formato válido.
            dados = form.cleaned_data() #converte os dados e 