import random


def gameMain():
    word = Word('words.txt')
    guess = Guess(word.randFromDB())
    hangman = Hangman()

    while hangman.remainingLives > 0:

        display = hangman.currentShape()
        print(display)
        display = guess.displayCurrent()
        print('Current: ' + display)
        display = guess.displayGuessed()
        print('Already Used: ' + display)

        guessedChar = input('Select a letter: ')
        if len(guessedChar) != 1:
            print('One character at a time!')
            continue
        if guessedChar in guess.guessedChars:
            print('You already guessed \"' + guessedChar + '\"')
            continue

        success = guess.guess(guessedChar)
        if success == False:
            hangman.decreaseLife()

        if guess.finished():
            break

    if guess.finished() == True:
        print('**** ' + guess.displayCurrent() + ' ****')
        print('Success')
    else:
        print(hangman.currentShape())
        print('word [' + guess.secretWord + ']')
        print('guess [' + guess.displayCurrent() + ']')
        print('Fail')


class Guess:
    def __init__(self, word):

        self.secretWord = word
        self.currentStatus = '_' * len(word)
        self.guessedChars = {'e', 'n'}
        self.guess('')

    def guess(self, character):

        self.guessedChars |= {character}
        if character not in self.secretWord:
            return False

        else:
            currentStatus = ''
            for c in self.secretWord:
                if c in self.guessedChars:
                    currentStatus += c
                else:
                    currentStatus += '_'

            self.currentStatus = currentStatus

            return True

    def finished(self):
        if self.currentStatus == self.secretWord:
            return True
        else:
            return False

    def displayCurrent(self):

        guessWord = ''
        for c in self.currentStatus:
            guessWord += (c + ' ')
        return guessWord

    def displayGuessed(self):

        guessed = ''
        for c in sorted(list(self.guessedChars)):
            guessed += (c + ' ')
        return guessed


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

    def __init__(self):
        self.remainingLives = len(self.text) - 1

    def decreaseLife(self):
        self.remainingLives -= 1

    def currentShape(self):
        return self.text[self.remainingLives]


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
    gameMain()
