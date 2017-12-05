import unittest

from guess import Guess

class TestGuess(unittest.TestCase):

    def setUp(self):
        self.g1 = Guess('default')

    def tearDown(self):
        pass

    def testDisplayCurrent(self):
        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ _ ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')

    def testDisplayGuessed(self):
        self.assertEqual(self.g1.displayGuessed(), ' e n ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a e n ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')
    def testGuess(self):
        self.assertEqual(self.g1.secretWord , 'default')
        self.assertEqual(self.g1.guess('a'),True)
        self.assertEqual(self.g1.currentStatus,'_e_a___')
        self.g1.guess('a')
        self.assertEqual(self.g1.guess('u'),True)
        self.g1.guess('u')
        self.assertEqual(self.g1.currentStatus,'_e_au__')
        self.assertEqual(self.g1.guess('w'),False)
        self.assertEqual(self.g1.secretWord, 'default')
        self.g1.guess('w')
        self.assertEqual(self.g1.secretWord ,'default')
        self.assertEqual(self.g1.currentStatus, '_e_au__')
        self.g1.guess('d')
        self.g1.guess('f')
        self.g1.guess('l')
        self.assertEqual(self.g1.finished(),False)
        self.g1.guess('t')
        self.assertEqual(self.g1.finished(),True)

if __name__ == '__main__':
    unittest.main()
