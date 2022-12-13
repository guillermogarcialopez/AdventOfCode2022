import numpy as np


'''******** Day 1 ********'''
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
##print(max(totalByElf))