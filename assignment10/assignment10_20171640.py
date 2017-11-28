import random


def game_main():
    word = Word('words.txt')
    guess = Guess(word.randFromDB())

    finished = False
    hangman = Hangman()
    maxTries = hangman.getLife()

    while guess.numTries < maxTries:

        display = hangman.get(maxTries - guess.numTries)
        print(display)
        guess.display()

        guessedChar = input('Select a letter: ')
        if len(guessedChar) != 1:
            print('One character at a time!')
            continue
        if guessedChar in guess.guessedChars:
            print('You already guessed \"' + guessedChar + '\"')
            continue

        finished = guess.guess(guessedChar)
        if finished is True:
            break

    if finished is True:
        print('Success')
    else:
        print(hangman.get(0))
        print('word [' + guess.secretWord + ']')
        print('guess [' + guess.currentStatus + ']')
        print('Fail')


class Guess:
    def __init__(self, word):
        self.word = word
        self.secret = word
        self.guessedChars = ["_"] * (len(self.secret))
        self.numTries = 0
        self.setlist = list(set(self.secret))
        self.c_num = 0
        self.locate = 0
        self.locate2 = 0
        self.locate3 = 0
        self.finish = 0
        self.used = []

    def display(self):
        print("Current :", self.guessedChars)
        print("Used word :", self.used)
        print("Tries :", self.numTries)

    def guess(self, character):
        n = 0
        self.used.append(character)
        for i in self.secret:
            if i == character:
                self.numTries += 0
                self.c_num = list(self.secret).count(i)
                for j in range(len(self.secret)):
                    self.locate = self.word.find(character)
                    if self.locate != -1:
                        for k in range(self.c_num):
                            del self.guessedChars[self.locate]
                            self.guessedChars.insert(self.locate, character)
                            self.locate2 = self.word.find(character, k + 1)
                            if self.locate2 != -1:
                                for m in range(self.c_num):
                                    del self.guessedChars[self.locate2]
                                    self.guessedChars.insert(self.locate2, character)
                                    self.locate3 = self.word.rfind(character)
                                    if self.locate3 != -1:
                                        for m in range(self.c_num):
                                            del self.guessedChars[self.locate3]
                                            self.guessedChars.insert(self.locate3, character)
                for l in range(len(self.secret)):
                    self.finish = self.guessedChars.count("_")
                    if self.finish == 0:
                        print("Current :", self.guessedChars)
                        print("Used word :", self.used)
                        print('Success')
                        exit(0)
                    break
            elif i != character:
                n += 1
                if n == len(self.secret):
                    self.numTries += 1
                    break
        if self.numTries == 6:
            print('''\
           ____
          |    |
          |    o
          |   /|\\
          |    |
          |   / \\
         _|_
        |   |______
        |          |
        |__________|\
        ''', )
            print('word [' + self.secret + ']')
            print('lasted try [' + str(self.numTries) + ']')
            print('Fail')
            exit(0)


class Hangman:
    text = [

        '''\
           ____
          |    |
          |    o
          |   /|\\
          |    |
          |   / \\
         _|_
        |   |______
        |          |
        |__________|\
        ''',

        '''\
           ____
          |    |
          |    o
          |   /|\\
          |    |
          |   /
         _|_
        |   |______
        |          |
        |__________|\
        ''',

        '''\
           ____
          |    |
          |    o
          |   /|\\
          |    |
          |
         _|_
        |   |______
        |          |
        |__________|\
        ''',

        '''\
           ____
          |    |
          |    o
          |   /|
          |    |
          |
         _|_
        |   |______
        |          |
        |__________|\
        ''',

        '''\
           ____
          |    |
          |    o
          |    |
          |    |
          |
         _|_
        |   |______
        |          |
        |__________|\
        ''',

        '''\
           ____
          |    |
          |    o
          |
          |
          |
         _|_
        |   |______
        |          |
        |__________|\
        ''',

        '''\
           ____
          |    |
          |
          |
          |
          |
         _|_
        |   |______
        |          |
        |__________|\
        ''',

    ]

    def getLife(self):
        return len(self.text) - 1

    def get(self, life):
        return self.text[life]


class Word:
    def __init__(self, filename):
        self.words = []
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()

        self.count = 0
        for line in lines:
            word = line.rstrip()
            self.words.append(word)
            self.count += 1

        print('%d words in DB' % self.count)

    def test(self):
        return 'default'

    def randFromDB(self):
        r = random.randrange(self.count)
        return self.words[r]


if __name__ == '__main__':
    game_main()
