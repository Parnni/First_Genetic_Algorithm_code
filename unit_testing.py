# Importing modules.
import unittest
from Guess_word_using_GA import guess

# Creating a test class.
class guess_class_test(unittest.TestCase):
    '''Testing the Guess_word_using_GA class.'''

    def setUp(self):
        # Arranging the values.
        print('Arranging the values.')
        self.string_test = 'Hello there.'

    def tearDown(self): 
        # Removing the values.
        print('Tearing down the values.')
        self.string_test = ''

    def test1(self):
        '''Checks whether the strings are same or not.'''

        print('Running test1.')

        # Number of iterations.
        iterations = 100000

        # Action.
        guess_class = guess(target_string = self.string_test, 
                            iterations = iterations)
        _, best_solution = guess_class.best_gene()

        # Assert.
        self.assertEqual(self.string_test, best_solution)

# Running the script.
if __name__ == '__main__':
    unittest.main()