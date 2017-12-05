import unittest

from assignment11_20171640 import Guess


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
        self.g1.guess('d')
        self.assertEqual(self.g1.displayCurrent(), 'd e _ a u _ t ')
        self.g1.guess('f')
        self.assertEqual(self.g1.displayCurrent(), 'd e f a u _ t ')
        self.g1.guess('l')
        self.assertEqual(self.g1.displayCurrent(), 'd e f a u l t ')

    def testDisplayGuessed(self):
        self.assertEqual(self.g1.displayGuessed(), ' e n ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a e n ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')
        self.g1.guess('d')
        self.assertEqual(self.g1.displayGuessed(), ' a d e n t u ')
        self.g1.guess('f')
        self.assertEqual(self.g1.displayGuessed(), ' a d e f n t u ')
        self.g1.guess('l')
        self.assertEqual(self.g1.displayGuessed(), ' a d e f l n t u ')

    def testNoneAlphabet(self):
        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')
        self.assertEqual(self.g1.displayGuessed(), ' e n ')
        self.g1.guess('7')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')
        self.assertEqual(self.g1.displayGuessed(), ' 7 e n ')
        self.g1.guess('=')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')
        self.assertEqual(self.g1.displayGuessed(), ' 7 = e n ')
        self.g1.guess('ㅎ')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')
        self.assertEqual(self.g1.displayGuessed(), ' 7 = e n ㅎ ')

    def testSetType(self):
        self.assertSetEqual(self.g1.guessedChars,{'','e','n'})

    def testFinish(self):
        self.assertFalse(self.g1.finished())
        self.g1.guess('a')
        self.assertFalse(self.g1.finished())
        self.g1.guess('t')
        self.assertFalse(self.g1.finished())
        self.g1.guess('u')
        self.assertFalse(self.g1.finished())
        self.g1.guess('d')
        self.assertFalse(self.g1.finished())
        self.g1.guess('f')
        self.assertFalse(self.g1.finished())
        self.g1.guess('l')
        self.assertTrue(self.g1.finished())


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGuess)
    unittest.TextTestRunner(verbosity=4).run(suite)
