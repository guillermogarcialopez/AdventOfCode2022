import numpy as np
from RockPaperScissorChoices import RockPaperScissorChoicesPartOne

'''******** Part One ********'''
##Open file
f = open("../files/Day2.txt", "r").read()

strategy = [el.split(sep=' ') for el in f.splitlines()]
singlePunctuations = list()

for choices in strategy:
    roundChoice = RockPaperScissorChoicesPartOne(choices)
    #print("El calculo de esta ronda: {0}".format(roundChoice.getRoundPunctuations()))
    singlePunctuations.append(roundChoice.getRoundPunctuations())


allPunctuations = np.array(singlePunctuations)
total = np.sum(allPunctuations)
print("Total punctuation: {0}".format(total))



'''******** Part Two ********'''








