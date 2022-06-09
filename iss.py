import json
import turtle  # Comando "pip install PythonTurtle" no Prompt de Comando
import urllib.request  # Comando "pip install urllib" no Prompt de Comando
import time


# Utilizando o módulo "Turtle" para ajustar os parâmetros da janela
janela = turtle.Screen()
janela.setup(1280, 720)
janela.setworldcoordinates(-220,-120,220,120)  # Determina os limites da tela onde a ISS poderá percorrer (ajustável)
janela.title("LOCALIZAÇÃO DA ISS")

# Exibe a imagem do Mapa-múndi na tela como plano de fundo
janela.bgpic("mapa.gif")
janela.register_shape("iss.gif")
iss = turtle.Turtle()
iss.shape("iss.gif")
iss.setheading(45)  # Orientação (ângulo) da movimentação da ISS na tela
iss.penup()  # Determina que a ISS não "desenhará" na tela ao mudar de posição

while True:
    # Exibe a posição correspondente da ISS, em tempo-real, utilizando a WebAPI
    url = "http://api.open-notify.org/iss-now.json"
    resposta = urllib.request.urlopen(url)
    resultado = json.loads(resposta.read())

    # Adiciona a localização da ISS
    localizar = resultado["iss_position"]
    lat = localizar['latitude']
    lon = localizar['longitude']

    # Determinando o tipo das variáveis de localização
    lat = float(lat)
    lon = float(lon)
    iss.goto(lon, lat)  # Atualiza a posição (lat, lon) da ISS no mapa

    # Atualiza a janela a cada 5 segundos
    time.sleep(5)
