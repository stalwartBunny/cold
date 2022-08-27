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
    loopNumber = 1
    player1Cards = []
    player2Cards = []
    loopStack = []
    player1Outcome = []
    player2Outcome = []
    terrain = "None"

    def __init__(self, player1Cards, player2Cards):
        self.player1Cards = player1Cards
        self.player2Cards = player2Cards

    def func(self):
        print("After calling the func method...")
        print(f"This loop is numbered {loopNumber}, contains {player1Cards} from player 1, {player2Cards} from player 2, has a stack of {loopStack}, a player 1 outcome of {player1Outcome}, a player 2 outcome of {player2Outcome}, and {terrain} as terrain.")
        print("....function end....")

Lock = Card("*", "None", "Lock The Loop", 0, 0, 0, "None")
Spark = Card("Spark", "Red", "None", 1, 0, 0, "None")
LightningBolt = Card("Lightning Bolt", "Yellow", "None", 3, 0, 0, "None")
FluidCounter = Card("Fluid Counter", "Blue", "None", 0, 3, 0, "None")
Nudge = Card("Nudge", "Green", "None", 0, 1, 0, "None")
LightningBolt.func()
FluidCounter.func()
Spark.func()
Nudge.func()

def draw():
    global hand1
    global hand2

    seed1 = random.randint(1,30)
    seed2 = random.randint(1,30)
    seed3 = random.randint(1,30)
    seed4 = random.randint(1,30)
    seed5 = random.randint(1,30)
    seed6 = random.randint(1,30)
    seed7 = random.randint(1,30)
    seed8 = random.randint(1,30)

    hand1 = [LightningBolt, LightningBolt, LightningBolt, Spark, Lock]
    hand2 = [FluidCounter, FluidCounter, Nudge, Nudge, Lock]
#hard coded hands for now



def submitA():
    print("Your hand consists of: ")
    while i < hand1.length - 1:
        print({hand1[i - 1]})
        i ++
    handCodeA = input("Submit your card selections in order for player A (1243) adding * to lock a loop instead (12*3)>> ")
    if handCodeA.length != 4:
        print("Something seems to be wrong with your submission, try again.")
        submitA()

def submitB():
    print("Your hand consists of: ")
    while i < hand2.length - 1:
        print({hand2[i - 1]})
        i ++
    handCodeB = input("Submit your card selections in order for player B (1243) adding * to lock a loop instead (12*3)>> ")
    if handCodeB.length != 4:
        print("Something seems to be wrong with your submission, try again.")
        submitB()

def calculateLoops():

        slotA = cardSlot(hand1.handCodeA[0], hand2.handCodeB[0])
        slotB = cardSlot(hand1.handCodeA[1], hand2.handCodeB[1])
        slotC = cardSlot(hand1.handCodeA[2], hand2.handCodeB[2])
        slotD = cardSlot(hand1.handCodeA[3], hand2.handCodeB[3])
#not configured for locks yet


        #to do, loop calculation



def main():
    global hp1
    global hp2

    deckA = [LightningBolt, LightningBolt, LightningBolt, LightningBolt]
    deckALive = []
    deckB = [FluidCounter, Nudge, FluidCounter, Nudge]
    deckBLive = []
    handCodeA = 0
    handCodeB = 0

    print(f"Welcome to Creatures of Light and Darkness. Submit cards to slots left-to-right and by their listing in your hand.")
    print("For example, a hand with [Lightning Bolt], [Lightning Bolt], [Fluid Counter], [Fluid Counter] submitted as 1234 puts bolt in slots 1 and 2, and Counter in 3 and 4.")
    print("Whereas 1324 submits as Bolt, Counter, Bolt, Counter.")
    print("If you wish to lock a loop, submit * instead of a card. Loops will automatically lock every five turns unless another loop is locked that turn, and will lock at first opprotunity starting with the tallest stack left to right.")


    while hp1 > 0 and hp2 > 0:
        draw() #to do (correctly, current setup hardcodes hands)
        submitA()
        submitB()
        calculateLoops() #to do

    if hp1 <= 0:
        print("Player 1 has lost. Player 2 is victorious.")
        exit()
    if hp2 <= 0:
        print("Player 2 has been defeated. Player 1 is the victor.")
        exit()
