import random
import json

def cria_matriz_nula(m ,n):
  lista = []
  aux = []
  for i in range(m):
    for j in range(n):
      aux.append('_')
    lista.append(aux)
    aux = []
  return lista

def montaTabuleiro(m):
  estrutura = ''
  j = '|'
  for i in range(len(m)):
    estrutura += "["+j.join(m[i])+']\n'
  print(estrutura)

def verificaPreenchido(m, posicao):
  flag = True
  if m[posicao[0]][posicao[1]] == 'x' or m[posicao[0]][posicao[1]] == 'o':
    flag = False
  return flag
  
def verificaGanhador(m, marcador):
  flag = True
  
  # verifica velha na diagonal
  if m[0][0] == marcador and m[1][1] == marcador and m[2][2] == marcador:
    flag = False
   
  # verifica velha na diagonal inverssa 
  if m[2][2] == marcador and m[1][1] == marcador and m[0][0] == marcador:
    flag = False
    
  somaHorizontal = 0
  for i in range(len(m[0])):
    for j in range(len(m)):
      if m[i][j] == marcador and flag:
        somaHorizontal += 1
        if somaHorizontal == 3:
          flag = False
    somaHorizontal = 0
  
  somaVertical = 0
  for i in range(len(m[0])):
    for j in range(len(m)):
      if m[j][i] == marcador and flag:
        somaVertical += 1
        if somaVertical == 3:
          flag = False
    somaVertical = 0

  return flag
  
def marcaJogada(m, posicao, marcador):
  m[posicao[0]][posicao[1]] = marcador

def verificaPosicoesVazia(m):
  aux = []
  for i in range(len(m)):
    for j in range(len(m[i])):
      if(m[i][j] == '_'):
        aux.append([i, j]);
  return aux

def jogadaAutomatica(m):
  livres = verificaPosicoesVazia(m)
  jogada = random.randint(0, len(livres)-1)
  return livres[jogada]


def tabuleiroCompleto(m):
  for i in range(len(m)):
    for j in range(len(m[i])):
      if(m[i][j] != '_'):
        return False
  return True

# Leitura de arquivos JSON
def readFileJson(file):
  fo = open(file, "r")
  jsonData = fo.read()
  if jsonData:
    jsonToPython = json.loads(jsonData)
    return jsonToPython
  return []

# Escrita em arquivos JSON
def writeFileJson(file, data):
  jsonFile = readFileJson(file)
  for d in data:
    jsonFile.append(d)
  aux = json.dumps(jsonFile)
  fo = open(file, 'w')
  fo.write(aux)

def convertArrayToTxt(arr):
  s = ''
  for a in arr:
    s += str(a[0])+str(a[1])
  return s

# Salva a partida do jogo
def saveMatchGame(match, winner):
  if(winner == 'X'):
    peso = ["100", "010"]
  elif(winner == 'O'):
    peso = ["010", "100"]
  else:
    peso = ["001", "001"]

  # Jogador X
  t1 = {
    "jogada": convertArrayToTxt(match[0]),
    "peso": peso[0]
  }
  # Jogador O
  t2 = {
    "jogada": convertArrayToTxt(match[1]),
    "peso": peso[1]
  }

  arr = [json.dumps(t1), json.dumps(t2)]
  j = ','.join(arr)
  j = '['+j+']'
  writeFileJson("memo.json", json.loads(j))


def init():
  flag_jogo = True
  matriz = cria_matriz_nula(3, 3)
  historicoJogadas = []
  partida = [[], []]
  marcador = ''
  winner = ''

  while flag_jogo:
    if(marcador != 'X'):
      marcador = 'X'
      jogada = [int(input("Informe a linha: ")), int(input("Informe a coluna: "))]
      if(verificaPreenchido(matriz, jogada)):
        marcaJogada(matriz, jogada, marcador)
        partida[0].append(jogada)
    else:
      marcador = 'O'
      jogada = jogadaAutomatica(matriz)
      marcaJogada(matriz, jogada, marcador)
      partida[1].append(jogada)








    if(verificaGanhador(matriz, marcador) != True):
      print('Ganhooooou !')
      flag_jogo = False
      winner = marcador
    elif(tabuleiroCompleto(matriz)):
      flag_jogo = False



    montaTabuleiro(matriz)

    # se o jogo acabar zera as jogadas
    if(flag_jogo != True):
      print saveMatchGame(partida, winner)

#=================================================  


init()