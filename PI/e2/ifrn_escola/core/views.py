from django.shortcuts import render

def index(request):
    contexto = {
        'nome_usuario':'Estudante IFRN',
    }
    return render(request, 'index.html', contexto)

def lista_disciplinas(request):
    contexto = {
    'disciplinas':[
        'Django',
        'Python',
        'HTML',
    ],
    }
    return render(request, 'disciplinas.html', contexto)

def autorizacao(request):
    contexto = {
        'autorizado':True
    }
    return render(request, 'autorizacao.html', contexto)

# Será usada para a 4 (biblioteca) e a 9 (detalhes)
def return_livros():
    return {
        'livros':[
            {'id':1, 
             'titulo':'A Seleção', 
             'autor':'Kiera Cass', 
             'ano':'2012',
             'descricao':'Muitas garotas sonham em ser princesas, mas este não é o caso de America Singer. Ela topa se inscrever na Seleção só para agradar a mãe, certa de que não será sorteada para participar da competição em que o príncipe escolherá sua futura esposa. Mas é claro que depois disso sua vida nunca mais será a mesma...'},

            {'id':2, 
             'titulo':'O alquimista', 
             'autor':'Paulo Coelho', 
             'ano':'1988',
             'descricao':'Combinando espiritualidade, sabedoria e misticismo, O alquimista é uma inspiradora e emocionante história de autodescoberta que vem transformando a vida de milhões de leitores ao redor do mundo há mais de trinta anos. Santiago, um jovem pastor da Andaluzia, parte rumo ao Egito em busca de um tesouro escondido entre as Pirâmides. O que ele não sabe é que sua jornada o levará a riquezas muito diferentes – e mais satisfatórias – do que ele estava esperando. Ao longo do caminho, uma cigana, um homem que se diz rei e um alquimista lhe indicam a direção em que deve seguir e o ajudam a perceber que o maior tesouro se encontra dentro dele mesmo. Com a prosa poética de Paulo Coelho, este romance encantador nos recorda da sabedoria de ouvir nossos corações, reconhecer as oportunidades da vida e, mais importante, sempre seguir nossos sonhos. '},

            {'id':3, 
             'titulo':'Memórias Póstumas de Brás Cubas', 
             'autor':'Machado de Assis', 
             'ano':'1881',
             'descricao':'A autobiografia de Brás Cubas começa quando morre o homem e nasce um autor. O filho de uma família da alta sociedade é um narrador-personagem que constantemente comenta a própria obra e provoca o leitor ao se dirigir diretamente a ele, relatando uma vida sem realizações e fadada ao vazio existencial. Brás Cubas pinta o pessimismo, a ironia e a indiferença da sociedade burguesa carioca de então. Seria a busca por esse retrato social que, a partir daí, guiaria os autores do fim do Segundo Império e influenciaria toda a literatura nacional. A essa trajetória, Machado empresta o domínio da narrativa. Suas inovações literárias afastam-no de qualquer autor de sua época, alçando-o ao patamar de mestres da literatura universal, como James Joyce e William Shakespeare, e ao posto de maior expoente das letras brasileiras.'},

            {'id':4, 
             'titulo':'O Encontro Marcado', 
             'autor':'Fernando Sabino', 
             'ano':'1988',
             'descricao':'Esta é a história de um jovem em desesperada procura de si mesmo e da verdadeira razão de sua vida. Quase absorvido por uma brilhante boêmia intelectual, seu drama interior evolui subterraneamente, expondo os equívocos fundamentais que vinham frustrando sua existência e sufocando sua vocação. O encontro marcado é a história de Fernando Sabino? Sim, mas não se trata de uma autobiografia. É a história atormentada de toda uma geração, naquilo que ela tem de essencialmente dramático. Em meio às confusões da vida, procura-se um valor que dê sentido à desconcertante experiência pessoal de quem trava um duelo de morte com a vocação furtiva. História de adolescência e juventude, de prazeres fugidios, desespero, cinismo, desencanto, melancolia, tédio, que se acumulam no espírito do jovem escritor Eduardo Marciano, um homem que amadurece num mundo desorientado. Ele vê seu matrimônio quebrar-se quando já não pode abdicar; por força de sua própria experiência, o suicídio deixa de ser uma solução. Nessa paisagem atormentada, ele deve renunciar a si mesmo, para comparecer ao encontro com uma antiga verdade.'},
        ],
    }

def biblioteca(request):
    contexto = return_livros()
    return render(request, 'biblioteca.html', context=contexto)

def prioridade(request):
    contexto = {
        'nivel_prioridade':3
    }
    return render(request, 'prioridade.html', context=contexto)

def lista_alunos(request):
    contexto = {
        'lista_alunos':[
            {'nome': 'Ana Maria Legal', 'matricula':'2025010001'},
            {'nome': 'Chatinho de Lins', 'matricula':'2025010002'},
            {'nome': 'Anderson Moura', 'matricula':'2025010003'},
            {'nome': 'Heitor Riquinho', 'matricula':'2025010004'},
            {'nome': 'Tigre de Bolinha', 'matricula':'2025010005'},
        ],
    }
    return render(request, 'lista_alunos.html', contexto)

def detalhes(request, livro_id):
    livros = return_livros()['livros']
    for livro in livros:
        if livro['id'] == int(livro_id):
            livro_detalhes = livro
    return render(request, 'detalhes.html', livro_detalhes)

def alerta(request):
    contexto={
        'mostrar_alerta':True,
    }
    return render(request, 'alerta.html', context=contexto)