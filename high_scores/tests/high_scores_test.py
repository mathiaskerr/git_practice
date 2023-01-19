import unittest

from src.high_scores import *

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):
    def setUp(self):
    
        self.scores = [5,47,45,4,80]
        self.scores_2 = [5,60,60,60,7]
        self.scores_3 = [90,99,80,99,20]
        self.scores_4 = [50,60]
        self.scores_6 = [20]

    def test_return_latest_score(self):
        self.assertEqual(80, latest(self.scores))

    def test_personal_best_score(self):
        self.assertEqual(80, personal_best(self.scores))
    
    def test_personal_top_three(self):
        self.assertEqual("1st Place 80, 2nd Place 47, 3rd Place 45" , personal_top_three(self.scores))
    
    def test_highest_to_lowest(self):
        self.assertEqual([80,47,45,5,4], sort_scores(self.scores))

    def test_highest_score_tie(self):
        self.assertEqual("Top Three scores tied at 60", tie_scores(self.scores_2))

    def test_top_two_scores_tied(self):
        self.assertEqual('1st and 2nd tied at 99 and 3rd place at 90', tie_scores(self.scores_3))    
    
    def test_2_scores(self):
        self.assertEqual('1st place 60 and 2nd place 50', tie_scores(self.scores_4))
    
    def test_1_score(self):
        self.assertEqual('you have the only score on the board at 20', tie_scores(self.scores_6))

    # Test latest score (the last thing in the list)

    # Test personal best (the highest score in the list)

    # Test top three from list of scores

    # Test ordered from highest tp lowest

    # Test top three when there is a tie

    # Test top three when there are less than three

    # Test top three when there is only one
    

