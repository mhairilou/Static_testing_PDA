import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card1 = Card('spades', 1)
        self.card2 = Card('clubs', 4)


        self.cards = [self.card1, self.card2]


    def test_card_has_suit(self):
        self.assertEqual('spades', self.card1.suit)

    def test_card_has_value(self):
        self.assertEqual(4, self.card2.value)

    def test_check_for_ace_true(self):
        result = CardGame.check_for_ace(self.card1)
        self.assertEqual(True, result)

    def test_check_for_ace_false(self):
        result = CardGame.check_for_ace(self.card2)
        self.assertEqual(False, result)

    def test_highest_card(self):
        result = CardGame.highest_card(self.card1, self.card2)
        self.assertEqual(self.card2, result)

    def test_cards_total(self):
        result = CardGame.cards_total(self.cards)
        self.assertEqual("You have a total of 5", result)
