import tkinter as tk  # Comando "pip install tk" no Prompt de Comando
from tkinter import *  # Importar todos os módulos do TKINTER
from subprocess import call  # Subprocesso "call" que "chama" (executa) outros programas
import PIL  # Comando "pip install Pillow" no Prompt de Comando
from PIL import ImageTk, Image  # Importa somente os módulos citados de PIL

# Variáveis globais que definem, respectivamente, a altura e a largura da janela
HEIGHT = 600
WIDTH = 1000

# Variáveis globais (com a descrição de todos os objetos) que serão exibidas no programa
INFO_MERCURIO = '\n\nO menor planeta do Sistema Solar \n e o mais próximo do sol, Mercúrio é apenas \num pouco maior que a Lua.\n\n\n Da superfície de Mercúrio, o Sol \n teria três vezes o seu tamanho aparente \n visto da Terra,\ne sua luminosidade seria \naté sete vezes maior.\n\n\n Apesar de sua \nproximidade com o Sol, Mercúrio não é o \nplaneta mais quente do nosso sistema solar, \nesse título pertence a Vênus, \ngraças à sua densa atmosfera.'

INFO_VENUS = '\n\nVênus é o segundo planeta a partir do Sol e \no nosso vizinho mais próximo.\n\n\nSemelhante em estrutura e tamanho à \nTerra, Vênus gira lentamente na direção oposta\nda maioria dos planetas.\nSua atmosfera espessa retém o calor\nem um efeito estufa descontrolado,\no tornando o planeta mais quente \ndo nosso sistema solar, com temperaturas\nde superfície suficientemente quentes \n para derreter chumbo.\n\n\nVislumbres abaixo das nuvens \nrevelam antigos vulcões e montanhas\ndeformadas.\n\n\n Vênus recebeu o nome da antiga deusa romana do amor \ne da beleza, que era conhecida como Afrodite, \nna Grécia Antiga.'

INFO_TERRA = '\n\nNosso planeta é o terceiro do Sistema Solar \n e o único lugar que conhecemos até agora que é habitado \npor seres vivos.\n\n\nEnquanto a Terra é apenas o quinto maior planeta\n do Sistema Solar, é o único lugar \nonde encontramos água líquida na superfície.\nApenas um pouco maior do que Vênus, a Terra é\no maior dos quatro planetas mais próximos do Sol,\n os quais são feitos de rocha e metal.\n\n\nO nome Terra tem pelo menos 1.000 anos.\nTodos os planetas, exceto a Terra, foram \n "batizados"com o nome de deuses gregos\ne romanos.\nNo entanto, o nome Terra é uma palavra germânica\nque significa simplesmente "o solo".'

INFO_MARTE = '\n\nSendo o quarto planeta a partir do Sol, \nMarte é um mundo empoeirado, frio e \ndesértico com uma atmosfera muito fina.\n\n\nEste planeta dinâmico tem estações, \ncalotas polares, cânions e \n vulcões. Evidências indicam que os vulcões\njá foram muito ativos, no passado.\n\n\n Marte é um dos corpos mais explorados \ndo nosso Sistema Solar e é o único planeta \npara onde enviamos rovers para percorrer \n e explorar o solo. \n\n\nAtualmente, a NASA tem três espaçonaves \n em órbita, um rover e um lander na superfície.\nA Índia e a ESA também têm espaçonaves em\nórbita marciana.\nEsses exploradores robóticos encontraram muitas \nevidências de que Marte era muito mais úmido e quente, \ncom uma atmosfera mais espessa, \nhá bilhões de anos atrás. A NASA lançou o rover \nPerseverance e o helicóptero Ingenuity \npara Marte em 30 de julho de 2020.'

INFO_JUPITER = '\n\nJúpiter tem uma longa história que surpreende \ncientistas desde 1610, quando Galileu Galilei \nencontrou as primeiras luas além da Terra. \nEssa descoberta mudou a forma como vemos o universo.\n\n\nO quinto em órbita do Sol, Júpiter é, \nde longe, o maior planeta do sistema solar \n(mais que o dobro da massa de todos os \noutros planetas combinados).\n\n\nAs listras familiares \ne tempestades de Júpiter são,\nna verdade, nuvens frias e velozes \n de amônia e água, flutuando em uma atmosfera de \nhidrogênio e hélio.\n\n\nA icônica Grande Mancha Vermelha de Júpiter \né uma tempestade gigante (maior que a Terra), que \nestá ativa há centenas de anos.'

INFO_SATURNO = '\n\n\nSaturno é o sexto planeta\na partir do Sol \ne o segundo maior planeta do\nnosso Sistema Solar.\n\n\nAdornado com milhares de lindos anéis,\n Saturno é único entre os planetas. Ele\nnão é o único planeta a ter anéis — feitos \nde pedaços de gelo e poeira — mas nenhum \né tão espetacular ou tão complicado\nquanto o de Saturno.\n\n\n Assim como o gigante gasoso Júpiter,\nSaturno é uma esfera massiva feita,\nprincipalmente,\nde hidrogênio e hélio.'

INFO_URANO = '\n\nO primeiro planeta encontrado com a\najuda de um telescópio,\nUrano foi descoberto em 1781\npelo astrônomo William Herschel,\n embora ele originalmente pensasse que\nera um cometa ou uma estrela.\n\n\nDois anos após sua descoberta,\nesse objeto foi universalmente aceito\ncomo um novo planeta, \nem parte por causa de observações\ndo astrônomo Johann Elert Bode.\n\n\nHerschel tentou, sem sucesso, nomear\nsua descoberta \nde "Georgium Sidus" em homenagem\n ao rei George III. Em vez disso, a \ncomunidade científica aceitou a sugestão\n de Bode em nomeá-lo \nUrano, o deus grego do céu.'

INFO_NETUNO = '\n\nEscuro, frio e açoitado por ventos\nsupersônicos, o simpático gigante Netuno \né o oitavo e mais distante planeta do \nnosso sistema solar.\n\n\nMais de 30 vezes mais distante do Sol que \na Terra, Netuno é o único planeta em nosso \nSistema Solar que não é visível \na olho nu e o primeiro previsto pela \nmatemática antes de sua descoberta. Em 2011, \nNetuno completou seus primeiros 165 anos \nde órbita desde sua descoberta em 1846.\n\n\n A Voyager 2 da NASA é a única espaçonave \nque visitou Netuno de perto. Ela o visitou \nem 1989, ao sair do sistema solar.'

INFO_SAGITTARIUS = '\n\nA imagem (divulgada em 12/05/2022)\né um olhar muito esperado para\no objeto maciço que fica no centro de\nnossa galáxia.\n\n\nOs cientistas já haviam visto estrelas\norbitando em torno de algo invisível,\ncompacto e muito massivo no centro\nda Via Láctea. Isso sugeriu fortemente que\neste objeto - conhecido como Sagittarius A*\n(lê-se Sagittarius-A-"Estrela") - é um buraco\nnegro, e essa imagem fornece a primeira evidência\nvisual direta dele.\n\n\nEmbora não possamos ver o buraco negro\nem si, porque ele é completamente escuro,\no gás brilhante ao seu redor revela uma\nassinatura reveladora: uma região central escura\n(chamada de sombra) cercada por uma\nestrutura brilhante em forma de anel.\nA nova visão captura a luz "dobrada" pela\npoderosa gravidade do buraco negro,\nque é 4 milhões de vezes mais massivo que\no nosso Sol e está a aproximadamente\n26 mil anos-luz da Terra.'

INFO_M87 = '\n\nEm 2019, astrônomos surpreenderam o mundo\ncom a primeira imagem de um buraco negro\nna história da humanidade. Em conferências de\nimprensa coordenadas em todo o mundo, pesquisadores\ndo EHT (Telescópio Horizonte de Eventos) revelaram\na primeira evidência visual direta do\nburaco negro supermassivo, chamado M87*\n(lê-se M87-"Estrela"), no centro da galáxia\nMessier 87 e sua sombra.\n\n\nApesar de ser altamente mais massivo que\no buraco negro no centro da Via Láctea,\nsendo, aproximadamente, 6,5 bilhões de vezes\nmais massivo que o Sol, o M87* está a cerca\nde 50 milhões de anos-luz de distância\nda Terra.\nEmbora isso possa parecer grande,\na imagem vista pelo EHT tem apenas cerca\nde 40 microarcsegundos de diâmetro\n(equivalente a medir o comprimento de um\ncartão de crédito na superfície da Lua,\nvisto da Terra).'

INFO_ISS = '\n\nA Estação Espacial Internacional (International\nSpace Station - ISS) é um laboratório espacial\ncompletamente concluído,\ncuja montagem em órbita começou em 1998\ne terminou oficialmente em 8 de julho de 2011.\n\n\nA estação encontra-se em uma órbita baixa, que\npossibilita ser vista da Terra a olho nu,\ne viaja a uma velocidade média de 27 700 km/h,\ncompletando 15,70 órbitas por dia.\nCom isso, os astronautas conseguem visualizar o\nnascer e o pôr do Sol, em média, cerca de\n16 vezes por dia.\n\n\nA Estação Espacial Internacional, junta à\nEstação Espacial Chinesa (já tripulada), representa\na atual permanência humana no espaço e tem sido\nmantida com tripulações\n(geralmmente, mais de três astronautas)\ndesde o ano 2000.\n\n\nO objetivo da missão colaborativa da ISS é,\nbasicamente, realizar experimentos\ne monitoramentos, uma vez que o laboratório\nnão está completamente exposto às avarias\ncausadas pela atmosfera terrestre.'

# Variáveis do nome da imagem e da sua descrição
imagem_nome = ""
texto_nome = ""

# Cria uma janela "raiz" a partir da biblioteca Tkinter
root = tk.Tk()
root.title('CARACTERÍSTICAS DOS PLANETAS')
root.resizable(0, 0)  # Define que a janela não poderá ser redimensionada

# Função "planeta" com o atributo "event" (evento), para quando um planeta é selecionado
def planeta(event):
    planeta_escolhido = clicado.get()  # Evento de quando um planeta, dentro da lista de planetas, é selecionado

    if planeta_escolhido == opcao[0]:  # -----------------------------------------> MERCÚRIO
        imagem_nome = "mercurio.png"  # Imagem exibida
        texto_nome = INFO_MERCURIO  # Informações exibidas
    
    elif planeta_escolhido == opcao[1]:  # -----------------------------------------> VÊNUS
        imagem_nome = "venus.png"
        texto_nome = INFO_VENUS

    elif planeta_escolhido == opcao[2]:  # -----------------------------------------> TERRA
        imagem_nome = "terra.png"
        texto_nome = INFO_TERRA

    elif planeta_escolhido == opcao[3]:  # -----------------------------------------> MARTE
        imagem_nome = "marte.png"
        texto_nome = INFO_MARTE
    
    elif planeta_escolhido == opcao[4]:  # -----------------------------------------> JÚPITER
        imagem_nome = "jupiter.png"
        texto_nome = INFO_JUPITER
    
    elif planeta_escolhido == opcao[5]:  # -----------------------------------------> SATURNO
        imagem_nome = "saturno.png"
        texto_nome = INFO_SATURNO
    
    elif planeta_escolhido == opcao[6]:  # -----------------------------------------> URANO
        imagem_nome = "urano.png"
        texto_nome = INFO_URANO

    elif planeta_escolhido == opcao[7]:  # -----------------------------------------> NETUNO
        imagem_nome = "netuno.png"
        texto_nome = INFO_NETUNO

    elif planeta_escolhido == opcao[8]:  # -----------------------------------------> BURACO NEGRO DA M87
        imagem_nome = "m87.png"
        texto_nome = INFO_M87

    elif planeta_escolhido == opcao[9]:  # -----------------------------------------> BURACO NEGRO DA VIA LÁCTEA
        imagem_nome = "sagittariusA.png"
        texto_nome = INFO_SAGITTARIUS

    elif planeta_escolhido == opcao[10]:  # -----------------------------------------> ESTAÇÃO ESPACIAL
        imagem_nome = "iss.png"
        texto_nome = INFO_ISS

    # Abre a imagem correspondente ao nome do planeta, inicialmente, com a largura de 400 pixels 
    imagem = Image.open(imagem_nome)
    largurabase = 400

    # Define uma "label" de 400x400 dentro da janela e exibe a imagem correspondente, ajustando-a ao tamanho da "label"
    canvas2 = tk.Canvas(root, height=400, width=400, bg='#000', bd=0, highlightthickness=0, relief='ridge')
    larg = (largurabase / float(imagem.size[0]))  # Redefine a imagem para a largura de 400 p
    altur = int((float(imagem.size[1]) * float(larg)))  # Redefine a imagem para a altura de 400 p
    imagem = imagem.resize((largurabase, altur), PIL.Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(imagem)
    item4 = canvas2.create_image(225, 210, image=photo)

    canvas2.place(relx=0.05, rely=0.1, relheight=0.8, relwidth=0.5)  # Define a posição em que a "label" se encontra na janela

    for widget in frame_descr.winfo_children():  # Ao selecionar um planeta, as definições anteriores apresentadas em tela são eliminadas para que somente o planeta selecionado seja exibido
        widget.destroy()
        
    frame_inicio.destroy()  # Substitui a janela inicial após selecionar um planeta
    

    # Define uma "label", onde o texto (definição) será exibido(a), e informa o texto e a fonte utilizada
    label_planeta = tk.Label(frame_descr, text=texto_nome, font=('Gadugi', 10), bg='#000', fg='white')
    label_planeta.pack()

    item4.pack()  # Método usado para "compactar" o que será exibido no programa em colunas

# Função "Open". Quando executada, abre (chama) a aplicação "app.py"
def Open1():
    call(["python", "app.py"])  # Open1 = Programa das Órbitas Planetárias

def Open2():
    call(["python", "iss.py"])  # Open2 = Programa da Estação Espacial

# Define um plano de fundo (canvas) onde as informações serão exibidas, com a altura e a largura da própria janela e cor preta (#000)
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='#000')
canvas.pack()

# Define um plano de fundo, onde a descrição dos planetas será exibida, sua cor, seu tamanho e sua posição 
frame_descr = tk.Frame(root, bg='#000')
frame_descr.place(relx=0.55, rely=0.1, relheight=1, relwidth=0.4)

# Define o conteúdo da janela inicial
frame_inicio = tk.Frame(root, bg='#000')
frame_inicio.place(relx=0, rely=0.1, relheight=1, relwidth=1)

# Lista com os nomes dos objetos a serem escolhidos
opcao = ['Mercúrio', 'Vênus', 'Terra', 'Marte', 'Júpiter', 'Saturno', 'Urano', 'Netuno', 'M87', 'Sagittarius', 'ISS']
clicado = StringVar()
clicado.set(opcao[2])  # Estabelece que o programa sempre iniciará com a opção [2] (Terra) pré-selecionada
lista = OptionMenu(root, clicado, *opcao, command=planeta)  # Cria o menu drop-down com todos os objetos da lista "opcao". "clicado" retorna o valor (objeto) selecionado para a função "planeta"
lista.place(relx=0.35, rely=0.01, relheight=0.05, relwidth=0.1)  # Define a posição e o tamanho do menu

# Cria mais dois botões e determina seu tamanho e posição
botao2 = tk.Button(canvas, text='Órbitas', command=Open1)  # Define que o comando do botão é acionar a função "Open1"
botao2.place(relx=0.45, rely=0.01, relheight=0.05, relwidth=0.1)
botao3 = tk.Button(canvas, text='ISS Track', command=Open2)  # Define que o comando do botão é acionar a função "Open2"
botao3.place(relx=0.55, rely=0.01, relheight=0.05, relwidth=0.1)

# Texto exibido na janela inicial
texto1 = '''
CENTRO UNIVERSITÁRIO JORGE AMADO (UNIJORGE)

AV3 - Técnicas e Linguagem de Programação

Professor: Leonardo Santana Almeida da Silva

Alunos:
Douglas Batista dos Reis
Pedro da Conceição Cardoso
Matheus Cabeceira dos Santos

================================================================================================================================================
Selecione um objeto na lista e pressione "ENTER" para exibir suas informações
Clique em "Órbitas" para exibir as órbitas dos planetas
Clique em "ISS Track" para exibir a localização aproximada da Estação Espacial
================================================================================================================================================
'''

# Define o conteúdo da janela inicial, o plano de fundo, a cor e a fonte
janela_inicial1 = tk.Label(frame_inicio, text=texto1, font=('Times New Roman', 19), bg='#000', fg='white')
janela_inicial1.pack()

# Evento de loop que mantém a janela sendo executada até que, intencionalmente, seja fechada
mainloop()
