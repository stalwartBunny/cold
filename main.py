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
handCodeA = ""
handCodeB = ""

class Card:

    name = "Generic Card Name"
    cardColor = "No Color"
    nativeEffects = []
    damage = 0
    block = 0
    regen = 0
    terrainEffects = []

    def __init__(self, name, cardColor, nativeEffects, damage, block, regen, terrainEffects):
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


class cardSlot():
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
#LightningBolt.func()
#FluidCounter.func()
#Spark.func()
#Nudge.func()

def draw():
    global hand1
    global hand2
    global deckALive
    global deckBLive


    print("You drew some cards.")
    hand1 = [Lock, deckALive[0], deckALive[1], deckALive[2], deckALive[3]]
    hand2 = [Lock, deckBLive[0], deckBLive[1], deckBLive[2], deckBLive[3]]

    del deckALive[3]
    del deckALive[2]
    del deckALive[1]
    del deckALive[0]
    del deckBLive[3]
    del deckBLive[2]
    del deckBLive[1]
    del deckBLive[0]

    shuffle()

def shuffle():
    global deckALive
    global deckBLive
    global deckB
    global deckA

    deckALiveLength = 0
    deckBLiveLength = 0
    for i in deckALive:
        deckALiveLength = deckALiveLength + 1
    for i in deckBLive:
        deckBLiveLength = deckBLiveLength + 1
    print(deckALiveLength)
    print(deckBLiveLength)
    print(f"this is deck A: {deckA}")
    print(f"this is deck B: {deckB}")
    if deckALiveLength < 4:
        deckALive = deckA
        random.shuffle(deckALive)
        print("Deck A has been reshuffled")
        print(deckA)
        print(deckALive)
    if deckBLiveLength < 4:
        deckBLive = deckB
        random.shuffle(deckBLive)
        print("Deck B has been reshuffled")
        print(deckB)
        print(deckBLive)


def submitA():
    global handCodeA
    global hand1
    handLength = 0

    lockCount = 0
    print("Your hand consists of: ")
    for item in hand1:
        print({item.name})
    handCodeA = input("Submit your card selections in order for player A (1243) adding 0 to lock a loop instead (1203)>> ")
    handCodeA = list(map(int, str(handCodeA)))


    print(type(handCodeA))
    print(handCodeA)
    for char in handCodeA:
        handLength + 1
    if handLength >=5:
        print("Something seems to be wrong with your submission, try again.")
        submitA()

    for char in handCodeA:
        if char is "0":
            lockCount = lockCount + 1
    if lockCount > 1:
        print("You cannot submit more than one lock per round, try again.")
        submitA()


def submitB():
    global handCodeB
    global hand2
    handLength = 0
    lockCount = 0
    print("Your hand consists of: ")
    for item in hand2:
        print({item.name})
    handCodeB = input("Submit your card selections in order for player B (1243) adding 0 to lock a loop instead (1203)>> ")
    handCodeB = list(map(int, str(handCodeB)))
    for char in handCodeA:
        handLength + 1
    if handLength >=5:
        print("Something seems to be wrong with your submission, try again.")
        submitB()
    for char in handCodeB:
        if char is "0":
            lockCount = lockCount + 1
    if lockCount > 1:
        print("You cannot submit more than one lock per round, try again.")
        submitB()

def calculateLoops():
    global hp1
    global hp2
    global handCodeA
    global handCodeB
    global hand1
    global hand2


    card1 = hand1[handCodeA[0]]
    card2 = hand1[handCodeA[1]]
    card3 = hand1[handCodeA[2]]
    card4 = hand1[handCodeA[3]]
    card5 = hand2[handCodeB[0]]
    card6 = hand2[handCodeB[1]]
    card7 = hand2[handCodeB[2]]
    card8 = hand2[handCodeB[3]]

    print(card1.name, card2.name, card3.name, card4.name)
    print(card5.name, card6.name, card7.name, card8.name)


    slotA = cardSlot(card1, card5)
    slotB = cardSlot(card2, card6)
    slotC = cardSlot(card3, card7)
    slotD = cardSlot(card4, card8)

    print(f"This is slot A, {slotA.player1Cards.name, slotA.player2Cards.name}, This is slot B {slotB.player1Cards.name, slotB.player2Cards.name} This is slotC {slotC.player1Cards.name, slotC.player2Cards.name}, This is slotD {slotD.player1Cards.name, slotD.player2Cards.name}")

    player2Outcome = slotA.player1Cards.damage - slotA.player2Cards.block
    player1Outcome = slotA.player2Cards.damage - slotA.player1Cards.block

    player2Outcome = player2Outcome + (slotB.player1Cards.damage - slotB.player2Cards.block)
    player1Outcome = player1Outcome + (slotB.player2Cards.damage - slotB.player1Cards.block)

    player2Outcome = player2Outcome + (slotC.player1Cards.damage - slotC.player2Cards.block)
    player1Outcome = player1Outcome + (slotC.player2Cards.damage - slotC.player1Cards.block)

    player2Outcome = player2Outcome + (slotD.player1Cards.damage - slotD.player2Cards.block)
    player1Outcome = player1Outcome + (slotB.player2Cards.damage - slotB.player1Cards.block)

    if player1Outcome > 0:
        hp1 = hp1 - player1Outcome
        print(f"Oh no! Player 1 has lost {player1Outcome} life! They sit at {hp1} remaining hitpoints.")
    else:
        print(f"There wasn't enough impact to take damage. Player 1 hp is: {hp1}")

    if player2Outcome > 0:
        hp2 = hp2 - player2Outcome
        print(f"Oh no! Player 2 has lost {player2Outcome} life! They sit at {hp2} remaining hitpoints.")
    else:
        print(f"There wasn't enough impact to take damage. Player 2 hp is: {hp2}")



def main():
    global hp1
    global hp2
    global deckA
    global deckB
    global deckALive
    global deckBLive

    deckA = [LightningBolt, LightningBolt, LightningBolt, LightningBolt, LightningBolt, LightningBolt, LightningBolt, LightningBolt, LightningBolt, LightningBolt, LightningBolt, LightningBolt, LightningBolt, LightningBolt, LightningBolt, LightningBolt, LightningBolt, LightningBolt, LightningBolt, LightningBolt, LightningBolt, LightningBolt, LightningBolt, LightningBolt, LightningBolt, LightningBolt, LightningBolt, LightningBolt, LightningBolt, LightningBolt]
    #deckA = [LightningBolt, LightningBolt, LightningBolt, Spark, Spark, Spark, LightningBolt, LightningBolt, LightningBolt, Spark, Spark, Spark, LightningBolt, LightningBolt, LightningBolt, Spark, Spark, Spark, LightningBolt, LightningBolt, LightningBolt, Spark, Spark, Spark, LightningBolt, LightningBolt, LightningBolt, Spark, Spark, Spark]
    #deckALive = [LightningBolt, LightningBolt, LightningBolt, Spark, Spark, Spark, LightningBolt, LightningBolt, LightningBolt, Spark, Spark, Spark, LightningBolt, LightningBolt, LightningBolt, Spark, Spark, Spark, LightningBolt, LightningBolt, LightningBolt, Spark, Spark, Spark, LightningBolt, LightningBolt, LightningBolt, Spark, Spark, Spark]
    deckALive = [LightningBolt, LightningBolt, LightningBolt, LightningBolt, LightningBolt, LightningBolt, LightningBolt, LightningBolt, LightningBolt, LightningBolt, LightningBolt, LightningBolt, LightningBolt, LightningBolt, LightningBolt, LightningBolt, LightningBolt, LightningBolt, LightningBolt, LightningBolt, LightningBolt, LightningBolt, LightningBolt, LightningBolt, LightningBolt, LightningBolt, LightningBolt, LightningBolt, LightningBolt, LightningBolt]
    deckB = [FluidCounter, Nudge, FluidCounter, Nudge, FluidCounter, FluidCounter, Nudge, FluidCounter, Nudge, FluidCounter, FluidCounter, Nudge, FluidCounter, Nudge, FluidCounter, FluidCounter, Nudge, FluidCounter, Nudge, FluidCounter, FluidCounter, Nudge, FluidCounter, Nudge, FluidCounter, FluidCounter, Nudge, FluidCounter, Nudge, FluidCounter]
    deckBLive = [FluidCounter, Nudge, FluidCounter, Nudge, FluidCounter, FluidCounter, Nudge, FluidCounter, Nudge, FluidCounter, FluidCounter, Nudge, FluidCounter, Nudge, FluidCounter, FluidCounter, Nudge, FluidCounter, Nudge, FluidCounter, FluidCounter, Nudge, FluidCounter, Nudge, FluidCounter, FluidCounter, Nudge, FluidCounter, Nudge, FluidCounter]
    random.shuffle(deckALive)
    random.shuffle(deckBLive)
    handCodeA = 0
    handCodeB = 0

    print(f"Welcome to Creatures of Light and Darkness. Submit cards to slots left-to-right and by their listing in your hand.")
    print("For example, a hand with [Lightning Bolt], [Lightning Bolt], [Fluid Counter], [Fluid Counter] submitted as 1234 puts bolt in slots 1 and 2, and Counter in 3 and 4.")
    print("Whereas 1324 submits as Bolt, Counter, Bolt, Counter.")
    print("If you wish to lock a loop, submit * instead of a card. Loops will automatically lock every five turns unless another loop is locked that turn, and will lock at first opprotunity starting with the tallest stack left to right.")


    while hp1 > 0 and hp2 > 0:
        draw()
        submitA()
        submitB()
        calculateLoops() #more left to do, only does attack and block

    if hp1 <= 0:
        print("Player 1 has lost. Player 2 is victorious.")
        exit()
    if hp2 <= 0:
        print("Player 2 has been defeated. Player 1 is the victor.")
        exit()

main()
