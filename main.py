import random

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

# def joinPartida(partida, marcador):
#   ret = ''
#   j = ''
#   for i in range(len(partida)):
#     ret += marcador


# Funcoes inteligentes
historicoJogadas = []

#def salvaPartida(h):


  
#=================================================  

flag_jogo = True

matriz = cria_matriz_nula(3, 3)

jogada = []
partida_p1 = []
partida_p2 = []

marcador = 'X' # jogo comeca com o computador

#montaTabuleiro(matriz)


while flag_jogo:  
  # se o ultimo a jogar foi o PC
  if(marcador != 'X'):
    marcador = 'X'
    respostaPosicao = [int(input("Informe a linha: ")), int(input("Informe a coluna: "))]
    jogada = respostaPosicao

    if(verificaPreenchido(matriz, jogada)):
      marcaJogada(matriz, jogada, marcador)
      partida_p1.append(jogada)
  else:
    marcador = 'O'
    jogada = jogadaAutomatica(matriz)
    marcaJogada(matriz, jogada, marcador)
    partida_p2.append(jogada)

  # zera a jogada
  jogada = []

  if(verificaGanhador(matriz, marcador) != True):
    print('Ganhooooou !')
    flag_jogo = False
  elif(tabuleiroCompleto(matriz)):
    flag_jogo = False

  # se o jogo acabar zera as jogadas
  if(flag_jogo != True):
    j = ''
    print(partida_p1)
    j.join(partida_p1)
    historicoJogadas[j] = partida_p1
    j.join(partida_p2)
    historicoJogadas[j] = partida_p2

  montaTabuleiro(matriz)
  print(historicoJogadas)