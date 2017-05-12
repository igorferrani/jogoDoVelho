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

def jogaVelha(m, jogador):
  m[jogador['jogada'][0]][jogador['jogada'][1]] = jogador['time']
  
def verificaGanhador(m, jogador):
  flag = True
  
  # verifica velha na diagonal
  if m[0][0] == jogador['time'] and m[1][1] == jogador['time'] and m[2][2] == jogador['time']:
    flag = False
   
  # verifica velha na diagonal inverssa 
  if m[2][2] == jogador['time'] and m[1][1] == jogador['time'] and m[0][0] == jogador['time']:
    flag = False
    
  somaHorizontal = 0
  for i in range(len(m[0])):
    for j in range(len(m)):
      if m[i][j] == jogador['time'] and flag:
        somaHorizontal += 1
        if somaHorizontal == 3:
          flag = False
    somaHorizontal = 0
  
  somaVertical = 0
  for i in range(len(m[0])):
    for j in range(len(m)):
      if m[j][i] == jogador['time'] and flag:
        somaVertical += 1
        if somaVertical == 3:
          flag = False
    somaVertical = 0

  return flag
  
def marcaJogada(m, jogador):
  m[jogador['jogada'][0]][jogador['jogada'][1]] = jogador['time']

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


# Funcoes inteligentes
historicoJogadas = []

#def salvaPartida(h):


  
#=================================================  

flag_jogo = True

matriz = cria_matriz_nula(3, 3)
player = {'jogada':[0, 0], 'time': 'x'}
pc = {'jogada':[0, 0], 'time': 'o'}
jogadas1 = []
jogadas2 = []

ultimo_jogou = 2

montaTabuleiro(matriz)

while flag_jogo:  
  # se o ultimo a jogar foi o PC
  if(ultimo_jogou != 1):
    player['jogada'][0] = int(input("Informe a linha: "))
    player['jogada'][1] = int(input("Informe a coluna: "))

    jogador = player

    if(verificaPreenchido(matriz, player['jogada'])):
      marcaJogada(matriz, player)
      ultimo_jogou = 1
      jogadas1.append(player['jogada'])
      jogadas = jogadas1
  else:
    pc['jogada'] = jogadaAutomatica(matriz)
    marcaJogada(matriz, pc)
    jogador = pc
    ultimo_jogou = 2
    jogadas2.append(pc['jogada'])
    jogadas = jogadas2

  if(verificaGanhador(matriz, jogador) != True):
    print('Ganhooooou !')
    flag_jogo = False
  elif(tabuleiroCompleto(matriz)):
    flag_jogo = False

  # se o jogo acabar zera as jogadas
  if(flag_jogo != True):
    historicoJogadas.append(jogadas)
    jogadas1 = []
    jogadas2 = []

  montaTabuleiro(matriz)
  print(historicoJogadas)