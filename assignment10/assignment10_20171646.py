class Guess:

    def __init__(self, word):
        self.secretWord = word # 단어를 받음(String)
        self.guessedChars=[] #추측한 character 리스트
        self.numTries=0 #시도한 횟수
        self.currentStatus="" # 단어가 표시 됨 ex) (_ _ _ _ _ _)
        self.indexList=[] #만약 character 가 추측한 단어에 있을 경우 그 단어의 추측한 character의 위치를 따로 표시
        for i in range(len(word)):
            self.currentStatus+=' _' # 단어의 길이만큼 "_" 추가

    def display(self):
        print("Current: "+self.currentStatus)
        print("Tries: "+str(self.numTries))

    def guess(self, character):
        self.currentStatus=''
        count=0
        self.guessedChars.append(character) #추측한 단어리스트에 추가

        for i in range(len(self.secretWord)): #추측한 character가 단어에 있을 경우  추측한 위치를 indexList에 추가
            if self.secretWord[i]==character:
                self.indexList.append(i)
                count=1
        if count==0: #만약 추측한 character가 단어에 없을 경우 numTries에 1 추가
            self.numTries+=1
        for i in range(len(self.secretWord)): # "_ _ _ _"에 맞춘 것이 있을 경우 "_ a _ _" 이런 식으로 바꿈
            if i in self.indexList: # 맞춘게 있다면 그 단어 ex) "a" 추가
                self.currentStatus+=" "+self.secretWord[i]
            else:
                self.currentStatus+=" _" #맞춘게 없다면 "_" 추가
                count=3 #아직 맞춘게 없다면 count=3
        if count!=3: #모든 걸 맞췄다면 True 아니면 False
            return True
        else:
            return False







