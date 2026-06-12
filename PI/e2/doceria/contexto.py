def return_context():
    nome_loja = 'Sweet Dreams'
    fundacao = 2009
    servicos = [
        'Doces',
        'Decoração',
        'Bolos',
    ]
    produtos = [
        {'nome':'Brownie', 'descricao':'Brownie macio por dentro e com casquinha por fora. São duas camadas de tamanho 5cmx5cm com recheio de ninho', 'preco':7.00},
        {'nome':'Red Velvet', 'descricao':'Bolo amanteigado vermelho, muito macio e com cobertura de ninho e morangos de decoração.', 'preco':35.00},
        {'nome':'Bolo de Abacaxi', 'descricao':'Bolo de abacaxi com recheio de ninho com abacaxi e cobertura de chantilly.', 'preco':52.00},
        {'nome':'Pudim', 'descricao':'Pudim feito com leite condensado. É lisinho e delicioso. O tamanho é médio.', 'preco':32.00},
        {'nome':'Bolo de Rolo', 'descricao':'Bolo de rolo com recheio de goiabada e finalização com açúcar de confeiteiro.', 'preco':30.00},
    ]

    return {
        'nome_loja':nome_loja,
        'ano_fundacao':fundacao,
        'servicos':servicos,
        'produtos':produtos,
    }
