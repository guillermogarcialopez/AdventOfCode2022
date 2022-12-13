import numpy as np


'''******** Part One ********'''
##Open file
f = open("../files/Day1.txt", "r").read()

foods = f.split(sep="\n")

calories = list()
elf = list()

for food in foods:
    if food != '':
        elf.append(int(food)) 
    else:
        calories.append(elf)
        elf = list()


totalByElf = [sum(np.array(elf)) for elf in calories ]

print("Total by elf: " + str(max(totalByElf)))


'''******** Part Two ********'''
totalByElfSorted = np.sort(np.array(totalByElf))
firstElf, secondElf, thirdElf = totalByElfSorted[-1], totalByElfSorted[-2], totalByElfSorted[-3]
topThreeTotal = firstElf + secondElf + thirdElf

print("Top three total calories: " + str(topThreeTotal))
