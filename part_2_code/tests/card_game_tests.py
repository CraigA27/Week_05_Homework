import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    

    def setUp(self):
        self.card = Card("Spades", 1)
        self.card1 = Card("Clubs", 6)
        self.card2 = Card("Hearts", 5)
        self.cards = [self.card, self.card1, self.card2]
        self.cardgame = CardGame()

    def test_check_for_ace_true(self):
        self.assertEquals(True, self.cardgame.check_for_ace(self.card))

    def test_check_for_ace_false(self):
        self.assertEquals(False, self.cardgame.check_for_ace(self.card1))

    def test_highest_card(self):
        self.assertEquals(self.card1, self.cardgame.highest_card(self.card1, self.card2))

    def test_cards_total(self):
        self.assertEquals("You have a total of 12", self.cardgame.cards_total(self.cards))