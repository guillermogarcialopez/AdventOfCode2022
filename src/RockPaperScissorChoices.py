class RockPaperScissorChoicesPartOne():
    def __init__(self, choices):
        self.elfChoice = choices[0]
        self.myChoice  = choices[1]
        
        #Elf choice
        self.elfChoosesRock     = (self.elfChoice == 'A')
        self.elfChoosesPaper    = (self.elfChoice == 'B')
        self.elfChoosesScissors = (self.elfChoice == 'C')
        
        #My choice
        self.IChooseRock     = (self.myChoice == 'X')
        self.IChoosePaper    = (self.myChoice == 'Y')
        self.IChooseScissor  = (self.myChoice == 'Z')

        #Winnings/draw/loses:
        self.elfWins = (self.elfChoosesRock and self.IChooseScissor) or (self.elfChoosesPaper and self.IChooseRock) or (self.elfChoosesScissors and self.IChoosePaper)
        self.iWin = (self.elfChoosesRock and self.IChoosePaper) or (self.elfChoosesPaper and self.IChooseScissor) or (self.elfChoosesScissors and self.IChooseRock)
        self.isDraw = (not self.elfWins and not self.iWin)

        #Punctuations by individual choice
        self.valueOfChoices = {'X': 1, 'Y': 2, 'Z': 3}

    
    def getRoundPunctuations(self):
        roundPunctuation = 0
        if self.iWin:
            roundPunctuation += 6 
            roundPunctuation += self.valueOfChoices[self.myChoice]
        elif self.elfWins:
            roundPunctuation += self.valueOfChoices[self.myChoice]
        elif self.isDraw:
            roundPunctuation += 3
            roundPunctuation += self.valueOfChoices[self.myChoice]
        else:
            raise Exception("Nor winning not lose or draw !!")

        return roundPunctuation
            

'''class RockPaperScissorChoicesPartTwo():
    def __init__(self, choices):
        self.elfChoice = choices[0]
        self.roundResult  = choices[1]

        #Elf choice
        self.elfChoosesRock     = (self.elfChoice == 'A')
        self.elfChoosesPaper    = (self.elfChoice == 'B')
        self.elfChoosesScissors = (self.elfChoice == 'C')

        #Result of round
        self.iLose = (self.roundResult == 'X')
        self.isDraw = (self.roundResult == 'Y')
        self.iWin = (self.roundResult == 'Z')

    def getMyChoice(self):
        myChoice = None
        if(self.elfChoosesRock and self.iLose):
            myChoice = '''

        
        
