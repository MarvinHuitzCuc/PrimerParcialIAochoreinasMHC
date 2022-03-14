from pyrsistent import l
'''Nombre: Marvin Estuardo Huitz Cuc
   Carnet: 1490-18-11402

'''
'''
Simula una partida, por medio grafico se pueden ver los movimientos que va realizando, no logre implementar, que se pudiera sumar un jugador humano, para que hiciere sus movimientos

En este juego acepta, que se 
'''


'''Definicion de las diferentes funciones usadas en el programa'''

def inicio(n):
    for key in ['queen','row','col','nwtose','swtone']:
        board[key] = {}
    for i in range(n):
        board['queen'][i] = -1
        board['row'][i] = 0
        board['col'][i] = 0
    for i in range(-(n-1),n):
        board['nwtose'][i] = 0
    for i in range(2*n-1):
        board['swtone'][i] = 0
        
def tablero():
    l = len(board['queen'].keys())
    for row in sorted(board['queen'].keys()):
        print("")
        for j in range(l):
            print("-----",end="")
        print("\n|", end="")
        for i in range(l):
            if i == board['queen'][row]:
                print(" Q |", end="")
            else:
                print("   |",end="")
    print("")
    for j in range(l):
        print("-----",end="")

def posilibre(i,j):
    return(board['row'][i] == 0 and board['col'][j] == 0 and board['nwtose'][j-i] == 0 and board['swtone'][j+i] == 0)

def agregarreina(i,j):
    board['queen'][i] = j
    board['row'][i] = 1
    board['col'][j] = 1
    board['nwtose'][j-i] = 1
    board['swtone'][j+i] = 1

def quitarreina(i,j):
    board['queen'][i] = -1
    board['row'][i] = 0
    board['col'][j] = 0
    board['nwtose'][j-i] = 0
    board['swtone'][j+i] = 0
    

def posreina(i):
    n = len(board['queen'].keys())
    for j in range(n):
        if posilibre(i,j):
            agregarreina(i,j)
            print("\nAgregando Reina:\ni:{} j:{} \n".format(i,j))
            tablero()
            if i == n-1:
                return(True)
            else:
                extendsoln = posreina(i+1)
            if extendsoln:
                return(True)
            else:
                quitarreina(i,j)
                print("\nQuitando Reina:\ni:{} \n".format(i,j))
    else:
        return(False)

board = {}
n = int(input("Ingresa el numero de Reinas? "))
inicio(n)
if posreina(0):
    print("\n\nSolucion Final")
    tablero()

