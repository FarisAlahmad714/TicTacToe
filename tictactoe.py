import unittest

#class TicTacToe():

    #def foo():
       # return "foo "

class TestTicTacToe(unittest.TestCase):

    def test_truth(self):
        print("pie")
        self.assertEqual(12 , 12)

unittest.main()