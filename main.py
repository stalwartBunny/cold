from sys import exit
import random

hp1 = 60
hp2 = 60
hand1 = []
hand2 = []
player1DrawMod = 0
player2DrawMod = 0
slotA = []
slotB = []
slotC = []
slotD = []
lockedLoops = []
turnCount = 0
deckA = []
deckB = []
terrainStack = []

class Card:

    name = "Generic Card Name"
    cardColor = "No Color"
    nativeEffects = []
    damage = 0
    block = 0
    regen = 0
    terrainEffects = []

    def __init__(self, name, cardColor, nativeEffects, damage, block, regen, terrainEffects, ):
        self.name = name
        self.cardColor = cardColor
        self.nativeEffects = nativeEffects
        self.damage = damage
        self.block = block
        self.regen = regen
        self.terrainEffects = terrainEffects

    def func(self):
        print("After calling the func method...")
        print(f"{self.name}'s color is {self.cardColor}, has these native effects: {self.nativeEffects}, deals {self.damage} damage, blocks {self.block}, regens {self.regen}, and transforms the terrain this way: {self.terrainEffects}.")
        print("....function end....")


class cardSlot:
    player1Cards = []
    player2Cards = []
    loopStack = []
    player1Outcome = []
    player2Outcome = []

LightningBolt = Card("Lightning Bolt", "Yellow", "None", 3, 0, 0, "None")
FluidCounter = Card("Fluid Counter", "Blue", "None", 0, 3, 0, "None")
LightningBolt.func()
FluidCounter.func()
print(LightningBolt.name)

def main():
    print(f"Welcome to Creatures of Light and Darkness. Submit cards to slots left-to-right and by their listing in your hand.")
    print("For example, a hand with [Lightning Bolt], [Lightning Bolt], [Fluid Counter], [Fluid Counter] submitted as 1234 puts bolt in slots 1 and 2, and Counter in 3 and 4.")
    print("Whereas 1324 submits as Bolt, Counter, Bolt, Counter.")
    print("If you wish to lock a loop, submit * instead of a card. Loops will automatically lock every five turns.")


    while hp1 > 0 and hp2 > 0:
        draw() #to do
        submitA() #to do
        submitB() #to do
        calculateLoops() #to do

    if hp1 <= 0:
        print("Player 1 has lost. Player 2 is victorious.")
        exit()
    if hp2 <= 0:
        print("Player 2 has been defeated. Player 1 is the victor.")
        exit()
