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
    owner = "Player 1"

    def __init__(name, cardColor, nativeEffects, damage, block, regen, terrainEffects, owner):
        self.name = name
        self.cardColor = cardColor
        self.nativeEffects = nativeEffects
        self.damage = damage
        self.block = block
        self.regen = regen
        self.terrainEffects = terrainEffects
        self.owner = owner

    def func(self):
        print("After calling the func method...")
        print(f"{self.name}'s color is {self.cardColor}, has these native effects: {self.nativeEffects}, deals {self.damage} damage, blocks {self.block}, regens {self.regen}, and transforms the terrain this way: {self.terrainEffects}, owned by: {owner}.")
        print("....function end....")


class cardSlot:
    player1Cards = []
    player2Cards = []
    loopStack = []
    player1Outcome = []
    player2Outcome = []

LightningBolt = Card("Lightning Bolt", "Yellow", "None", 3, 0, 0, "None", "Player 2")
#LightningBolt.func()
print(LightningBolt.owner)
print(LightningBolt.name)
