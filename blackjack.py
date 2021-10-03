#zona de import
import pygame
from pygame import *
from enum import Enum,IntEnum
import random



#######################crear la interfaz grafica#######################
pygame.init()

VENTANA = pygame.display.set_mode([710,440])
tiempo = pygame.time.Clock()
pygame.display.set_caption("Mesa de Blackjack")

fondo = pygame.image.load("fondo.png").convert()

run_game = True

while run_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False #para cerrarlo solo es darle a la X
    
    VENTANA.blit(fondo,[0,0])
    pygame.display.flip()
    tiempo.tick(60)

pygame.quit()
####################Boton#######################
#################clase carta#######################
class Carta():
    def __init__(self,suit,simbolo,valor,color):
        self.value = suit
        self.value = simbolo
        self.value = valor
        self.value = color

#datos de las cartas
Valor_carta = [11,2,3,4,5,6,7,8,9,10,10,10]
Simbolo_carta = list(range(1,14))
Suit_carta = list(range(1,5))

#########################clase dealer#####################

class Dealer():
    def dealer():
        deck = []
        for j in range(len(Valor_carta)):
            for k in Suit_carta:
                deck.append(Carta(Valor_carta[j],Simbolo_carta[j],k))

        return deck

original_deck = Dealer()
full_deck = list(original_deck)

#########################Clase player#########################



########################Repartir cartas######################
#valores iniciales en las manos del jugador y del IA
player_hand = []
IA_hand = []
##Buscar las cartas dentro del array
def buscar_carta(valor,suit):
    if suit == 'pica':
        T = 1
    elif suit == 'trebol':
        T = 2
    elif suit == 'diamante':
        T = 3
    elif suit == 'corazon':
        T = 4
    else:
        print("error")
    
    return (valor-1)*4 + (T-1)

 #seleccion de carta al azar
def obtener_carta_random():
    global full_deck
    Random = random.randint(0,len(full_deck)-1)

    return full_deck.pop(Random)

#asiganar una carta en la mano del jugador
def jugador_elije_carta():
    player_hand.append(obtener_carta_random())

#asignar carta a la mano del IA
def IA_elije_carta():
    if obtener_valor_carta(IA_hand) < 17:
        IA_hand.append(obtener_carta_random())

        return True

    else:
        return False

#obtener el valor de las cartas del jugador / IA
def obtener_valor_carta(mano):
    if len(mano) == 0: #si la mano esta vacia obtener 8
        return 0
    else:
        Aces = []
        suma = 0

        for i in mano:
            if i.simbolo == 1:
                Aces.append(i)
            
            suma += i.valor
        
        if suma > 21 and (len(Aces) != 0): #cuando la suma es mas de 21 y hay un As
            suma -= 10
        return suma

## el jugador decide elejir otra carta


#