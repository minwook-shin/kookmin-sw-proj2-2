class Guess:

    def __init__(self, word):
        self.secretWord = word
        self.secretcharacterlist=[]
        self.guessedChars=[]
        self.numTries=0
        self.currentStatus=""
        for i in range(len(word)):
            self.secretcharacterlist.append([word[i],0])
            self.currentStatus+=' _'

    def display(self):
        print("Current: "+self.currentStatus)
        print("Tries: "+str(self.numTries))

        



    def guess(self, character):
        self.currentStatus=''
        count=0
        self.guessedChars.append(character)
        for i in range(len(self.secretWord)):
            if self.secretcharacterlist[i][0]==character:
                self.secretcharacterlist[i][1]=1
                count=1
        if count==0:
            self.numTries+=1
        for i in range(len(self.secretWord)):
            if self.secretcharacterlist[i][1]==1:
                self.currentStatus+=" "+self.secretcharacterlist[i][0]
            else:
                self.currentStatus+=" _"
                count=3
        if count!=3:
            return True
        else:
            return False







