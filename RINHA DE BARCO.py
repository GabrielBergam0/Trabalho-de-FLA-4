import random
barcos1 = 0
BARCO = u"\u2588\u2588"
BARCO_ATINGIDO = "##"
EMPTY = '@'.center(2)
MISS = ")("

#=============================================================================
#=============================================================================
def tem_barco(tabuleiro):
    
    global BARCO
    for line in tabuleiro:
        if u"\u2588\u2588" in line:
            return True
        else:
            return False
            print("FIM DE JOGO, EXISTE UM GANHADOR!!!")
            break
    

#=============================================================================
#=============================================================================

def cria_tabuleiro(n):
    tab = []
    for i in range(n):
        line = []
        for j in range(n * i, n * i + n, 1):
            line.append(EMPTY.center(2))
        tab.append(line)
    return tab

#=============================================================================
#=============================================================================

def mostra_tabuleiro(tab, vez = True):
    global BARCO_ATINGIDO, EMPTY
    n= len(tab[0])
    print("    01  | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 ")
    print("   --------------------------------------------------")
    for i in range(n):
        line = [c if (c == BARCO_ATINGIDO or c == MISS or vez) else EMPTY for c in tab[i]]
        print(chr(ord('A') + i) + "  " + (("| %s " * n) % tuple(line)) ) 
        if i < (n - 1): print("---|----|----|----|----|----|----|----|----|----|----") 
    print("   --------------------------------------------------")
    
#=============================================================================
#=============================================================================

def get_pos():
    pos = input("Digite a posição onde deseja colocar o barco acima : ").split(',')
    linha = ord(pos[0]) - ord('A')
    coluna = int(pos[1]) - 1
    while not (0 <= linha <=  9 and 0 <= coluna <=  9):
        print("Voce esta saindo do oceano! Tente novamente!")
        pos = input("Digite a posição onde deseja colocar o barco acima : ").split(',')
        linha = ord(pos[0]) - ord('A')
        coluna = int(pos[1]) - 1
    return linha, coluna


#=============================================================================
#=============================================================================
def get_random_pos():
    linhas = ["A","B","C","D","E","F","G","H","I","J"]
    colunas = ["1","2","3","4","5","6","7","8","9","10"]
    letra = random.choice(linhas)
    numero = random.choice(colunas)
    linha = ord(letra) - ord('A')
    coluna = int(numero) - 1
    return linha, coluna





#=============================================================================
#=============================================================================


Tabuleiro1 = cria_tabuleiro(10)
Tabuleiro2 = cria_tabuleiro(10)


#=============================================================================
#=============================================================================

def barcodepatrulha(tabuleiro, linha, coluna, direcao):
    try:
        if direcao == "H" or direcao == "h":
            if (not (tabuleiro[linha][coluna] == u"\u2588\u2588" or \
                     tabuleiro[linha][coluna +1] == u"\u2588\u2588")) and coluna +2 <= len(tabuleiro):
                tabuleiro[linha][coluna +1] = u"\u2588\u2588"
                tabuleiro[linha][coluna] = u"\u2588\u2588"
                return True
                  
        elif direcao == "V" or direcao == "v":
            if (not (tabuleiro[linha][coluna] == u"\u2588\u2588" or \
                     tabuleiro[linha +1][coluna] == u"\u2588\u2588")) and linha + 2 <= len(tabuleiro):
                tabuleiro[linha +1][coluna] = u"\u2588\u2588"
                tabuleiro[linha][coluna] = u"\u2588\u2588"
                return True
    except:
        return False

#modelo
#=============================================================================                  
#=============================================================================

def destroyer(tabuleiro, linha, coluna, direcao):
    try:
        if direcao == "H" or direcao == "h":
            if  (not (tabuleiro[linha][coluna] == u"\u2588\u2588" or \
                      tabuleiro[linha][coluna +1] == u"\u2588\u2588" or \
                      tabuleiro[linha][coluna +2] == u"\u2588\u2588")) and coluna + 3 <= len(tabuleiro):
                tabuleiro[linha][coluna +1] = u"\u2588\u2588"
                tabuleiro[linha][coluna +2] = u"\u2588\u2588"
                tabuleiro[linha][coluna] = u"\u2588\u2588"
                return True

                
        elif direcao == "V" or direcao == "v":
            if ( not (tabuleiro[linha][coluna] == u"\u2588\u2588" or \
                      tabuleiro[linha +1][coluna] == u"\u2588\u2588" or \
                      tabuleiro[linha +2][coluna] == u"\u2588\u2588")) and linha + 3 <= len(tabuleiro):
                tabuleiro[linha +1][coluna] = u"\u2588\u2588"
                tabuleiro[linha +2][coluna] = u"\u2588\u2588"
                tabuleiro[linha][coluna] = u"\u2588\u2588"
                return True
    except:
        return False
            

#=============================================================================
#=============================================================================
            
def submarino(tabuleiro, linha, coluna, direcao):
    try:
        if direcao == "H" or direcao == "h":
            if (not (tabuleiro[linha][coluna] == u"\u2588\u2588" or \
                    tabuleiro[linha][coluna +1] == u"\u2588\u2588" or \
                    tabuleiro[linha][coluna +2] == u"\u2588\u2588" or \
                    tabuleiro[linha][coluna +3] == u"\u2588\u2588")) and coluna + 4 <= len(tabuleiro):
                tabuleiro[linha][coluna +1] = u"\u2588\u2588"
                tabuleiro[linha][coluna +2] = u"\u2588\u2588"
                tabuleiro[linha][coluna +3] = u"\u2588\u2588"
                tabuleiro[linha][coluna] = u"\u2588\u2588"
                return True

                
        elif direcao == "V" or direcao == "v":
            if (not (tabuleiro[linha][coluna] == u"\u2588\u2588" or \
                     tabuleiro[linha +1][coluna] == u"\u2588\u2588" or \
                     tabuleiro[linha +2][coluna] == u"\u2588\u2588" or \
                     tabuleiro[linha +3][coluna] == u"\u2588\u2588")) and linha + 4 <= len(tabuleiro):
                tabuleiro[linha +1][coluna] = u"\u2588\u2588"
                tabuleiro[linha +2][coluna] = u"\u2588\u2588"
                tabuleiro[linha +3][coluna] = u"\u2588\u2588"
                tabuleiro[linha][coluna] = u"\u2588\u2588"
                return True
    except:
        return False


#=============================================================================
#=============================================================================
            
def porta_avioes(tabuleiro, linha, coluna, direcao):
    try:
        if direcao == "H" or direcao == "h":
            if (not(tabuleiro[linha][coluna] == u"\u2588\u2588" or \
                    tabuleiro[linha][coluna +1] == u"\u2588\u2588" or \
                    tabuleiro[linha][coluna +2] == u"\u2588\u2588" or \
                    tabuleiro[linha][coluna +3] == u"\u2588\u2588" or \
                    tabuleiro[linha][coluna +4] == u"\u2588\u2588")) and coluna + 5 <= len(tabuleiro):
                tabuleiro[linha][coluna +1] = u"\u2588\u2588"
                tabuleiro[linha][coluna +2] = u"\u2588\u2588"
                tabuleiro[linha][coluna +3] = u"\u2588\u2588"
                tabuleiro[linha][coluna +4] = u"\u2588\u2588"
                tabuleiro[linha][coluna] = u"\u2588\u2588"
                return True

        elif direcao == "V" or direcao == "v":
            if (not(tabuleiro[linha][coluna] == u"\u2588\u2588" or \
                    tabuleiro[linha +1][coluna] == u"\u2588\u2588" or\
                    tabuleiro[linha +2][coluna] == u"\u2588\u2588" or\
                    tabuleiro[linha +3][coluna] == u"\u2588\u2588" or\
                    tabuleiro[linha +4][coluna] == u"\u2588\u2588")) and linha + 5 <= len(tabuleiro):
                tabuleiro[linha +1][coluna] = u"\u2588\u2588"
                tabuleiro[linha +2][coluna] = u"\u2588\u2588"
                tabuleiro[linha +3][coluna] = u"\u2588\u2588"
                tabuleiro[linha +4][coluna] = u"\u2588\u2588"
                tabuleiro[linha][coluna] = u"\u2588\u2588"
                return True

    except:
        return False

                  
#=============================================================================
#=============================================================================
            
def encouraçado(tabuleiro, linha, coluna, direcao):
    try:
        if direcao == "H" or direcao == "h":
            if (not (tabuleiro[linha][coluna] == u"\u2588\u2588" or \
                     tabuleiro[linha][coluna +1] == u"\u2588\u2588" or \
                     tabuleiro[linha][coluna +2] == u"\u2588\u2588" or \
                     tabuleiro[linha][coluna +3] == u"\u2588\u2588" or \
                     tabuleiro[linha][coluna +4] == u"\u2588\u2588" or \
                     tabuleiro[linha][coluna +5] == u"\u2588\u2588")) and coluna + 6 <= len(tabuleiro):
                tabuleiro[linha][coluna +1] = u"\u2588\u2588"
                tabuleiro[linha][coluna +2] = u"\u2588\u2588"
                tabuleiro[linha][coluna +3] = u"\u2588\u2588"
                tabuleiro[linha][coluna +4] = u"\u2588\u2588"
                tabuleiro[linha][coluna +5] = u"\u2588\u2588"
                tabuleiro[linha][coluna] = u"\u2588\u2588"
                return True
            

        elif direcao == "V" or direcao == "v":
            if (not ( tabuleiro[linha][coluna] == u"\u2588\u2588" or \
                     tabuleiro[linha +1][coluna] == u"\u2588\u2588" or \
                     tabuleiro[linha +2][coluna] == u"\u2588\u2588" or \
                     tabuleiro[linha +3][coluna] == u"\u2588\u2588" or \
                     tabuleiro[linha +4][coluna] == u"\u2588\u2588" or \
                     tabuleiro[linha +5][coluna] == u"\u2588\u2588")) and linha + 6 <= len(tabuleiro):
                tabuleiro[linha +1][coluna] = u"\u2588\u2588"
                tabuleiro[linha +2][coluna] = u"\u2588\u2588"
                tabuleiro[linha +3][coluna] = u"\u2588\u2588"
                tabuleiro[linha +4][coluna] = u"\u2588\u2588"
                tabuleiro[linha +5][coluna] = u"\u2588\u2588"
                tabuleiro[linha][coluna] = u"\u2588\u2588"
                return True
            
    except:
        return False
#=============================================================================
#=============================================================================

def atack():
    pos = input("Digite a posição onde deseja lançar um missil : ").split(',')
    linha = ord(pos[0]) - ord('A')
    coluna = int(pos[1]) - 1
    while not (0 <= linha <=  9 and 0 <= coluna <=  9):
        print("Voce esta saindo do oceano! Tente novamente!")
        pos = input("Digite a posição onde deseja lançar um missil : ").split(',')
        linha = ord(pos[0]) - ord('A')
        coluna = int(pos[1]) - 1
    return linha, coluna

#=============================================================================
#=============================================================================
def ran_atack():
    linha = random.choice(["A","B","C","D","E","F","G","H","I","J"])
    coluna = random.choice(["1","2","3","4","5","6","7","8","9","10"])

    linha = ord(linha) - ord('A')
    coluna = int(coluna) - 1
    return linha,coluna
#=============================================================================
#=============================================================================

print("Ola, seja bem vindo ao meu codigo de batalha naval, carinhosmente apelidado de Rinha de Barco")
print("Para jogar basta digitar a direção e a posicao desejada no formato Letra,numero...(A,1) ")
print(" ")
print("Este é o seu tabuleiro: ")
print(" ")
mostra_tabuleiro(Tabuleiro1)
print(" ")
print("Este é o tabuleiro do inimigo: ")
print(" ")
mostra_tabuleiro(Tabuleiro2, False)

#--------------------------------------------------------------
print("Posicione um barco de patrulha 2x1")
direcao = str(input("Digite H para horizontal e V para vertical: "))
linha, coluna = get_pos()
while not barcodepatrulha(Tabuleiro1, linha, coluna, direcao):
    print("Voce nao pode colocar este barco ai!")         
    direcao = str(input("Digite H para horizontal e V para vertical: "))
    linha, coluna = get_pos()
    

linha, coluna = get_random_pos()
direcao = random.choice(['H', 'V'])
while not barcodepatrulha(Tabuleiro2, linha, coluna, direcao):
    linha, coluna = get_random_pos()

mostra_tabuleiro(Tabuleiro1)
print(" ")
mostra_tabuleiro(Tabuleiro2, False)

#--------------------------------------------------------------

print("Posicione um barco de destroyer 3x1")
direcao = str(input("Digite H para horizontal e V para vertical: "))
linha, coluna = get_pos()
while not destroyer(Tabuleiro1, linha, coluna, direcao):
    print("Voce nao pode colocar este barco ai!")
    direcao = str(input("Digite H para horizontal e V para vertical: "))
    linha, coluna = get_pos()

linha, coluna = get_random_pos()
direcao = random.choice(['H', 'V'])
while not destroyer(Tabuleiro2, linha, coluna, direcao):
    linha, coluna = get_random_pos()

mostra_tabuleiro(Tabuleiro1)
print(" ")
mostra_tabuleiro(Tabuleiro2, False)

#--------------------------------------------------------------

print("Posicione um barco de submarino 3x1")
direcao = str(input("Digite H para horizontal e V para vertical: "))
linha, coluna = get_pos()
while not destroyer(Tabuleiro1, linha, coluna,direcao):
    print("Voce nao pode colocar este barco ai!")
    direcao = str(input("Digite H para horizontal e V para vertical: "))
    linha, coluna = get_pos()

direcao = random.choice(['H', 'V'])
linha, coluna = get_random_pos()
while not submarino(Tabuleiro2, linha, coluna, direcao):
    linha, coluna = get_random_pos()

mostra_tabuleiro(Tabuleiro1)
print(" ")
mostra_tabuleiro(Tabuleiro2, False)


#--------------------------------------------------------------
print("Posicione um barco de porta-avioes 5x1")
direcao = str(input("Digite H para horizontal e V para vertical: "))
linha, coluna = get_pos()
while not porta_avioes(Tabuleiro1, linha, coluna, direcao):
    print("Voce nao pode colocar este barco ai!")
    direcao = str(input("Digite H para horizontal e V para vertical: "))
    linha, coluna = get_pos()

direcao = random.choice(['H', 'V'])
linha, coluna = get_random_pos()
while not porta_avioes(Tabuleiro2, linha, coluna, direcao):
    linha, coluna = get_random_pos()

mostra_tabuleiro(Tabuleiro1)
print(" ")
mostra_tabuleiro(Tabuleiro2, False)


#--------------------------------------------------------------
print("Posicione um barco de encouraçado 6x1")
direcao = str(input("Digite H para horizontal e V para vertical: "))
linha, coluna = get_pos()
while not encouraçado(Tabuleiro1, linha, coluna, direcao):
    print("Voce nao pode colocar este barco ai!")
    direcao = str(input("Digite H para horizontal e V para vertical: "))
    linha, coluna = get_pos()

direcao = random.choice(['H', 'V'])
linha, coluna = get_random_pos()
while not encouraçado(Tabuleiro2, linha, coluna, direcao):
    linha, coluna = get_random_pos()
    

mostra_tabuleiro(Tabuleiro1)
print(" ")
mostra_tabuleiro(Tabuleiro2, False)

    

#--------------------------------------------------------------
def tem_barco(Tabuleiro2):
    global BARCO
    for line in Tabuleiro2:
        if BARCO in line:
            return False
    return True
    print("JOGO ENCERRADO, EXISTE UM GANHADOR")

while not tem_barco(Tabuleiro2):
    linha,coluna = atack()
    if Tabuleiro2[linha][coluna] == (u"\u2588\u2588"):
        Tabuleiro2[linha][coluna] = (BARCO_ATINGIDO)
    else:
        Tabuleiro2[linha][coluna] = (MISS)

    linha, coluna = ran_atack()
    if Tabuleiro1[linha][coluna] == (u"\u2588\u2588"):
        Tabuleiro1[linha][coluna] = (BARCO_ATINGIDO)
    else:
        Tabuleiro1[linha][coluna] = (MISS)

    mostra_tabuleiro(Tabuleiro1)
    print(" ")
    mostra_tabuleiro(Tabuleiro2, False)







