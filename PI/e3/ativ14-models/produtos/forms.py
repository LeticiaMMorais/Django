from django import forms

class CriarProdutoForm(forms.Form):
    nome = forms.CharField(label="Nome do produto", max_length=150, required=True)
    categoria = forms.CharField(label="Categoria do produto", max_length=150)
    quantidade = forms.NumberInput(label="Quantidade")
    lote = forms.CharField(label="Lote do produto", max_length=5, required=True)
