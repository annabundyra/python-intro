import unittest 
from unittest.mock import patch 
from shop import purchased, retry_purchase, ThreeFailedAttempts, greeting, validate_item

# prices = {"TV": 1000, "Phone": 50, "Alarm Clock": 25}
class TestingInputs(unittest.TestCase):
    # INVALID USER INPUT
    @patch('builtins.input', return_value='Headphones')
    def test_invalid_item(self, item):
        self.assertRaises(ValueError, greeting)

    # VALID INPUT
    def test_valid_input_item(self):
        self.assertTrue(validate_item('Phone'))
    
    # INVALID INPUT
    def test_invalid_input_item(self):
        self.assertFalse(validate_item('Speaker'))

class TestingPurchased(unittest.TestCase):
    # VALID case
    def test_purchased_with_enough_money(self):
        self.assertEqual(True, purchased(item='Phone', balance=100))

    # INVALID CASE
    def test_purchased_with_not_enough_money(self):
        self.assertFalse(purchased(item='TV', balance=100))

    # Edge CASE
    def test_purchased_with_just_enough_money(self):
        self.assertTrue(purchased(item="TV", balance=1000))

class TestingRetryPurchase(unittest.TestCase):
    # test custom error is raised
    def test_retry_purchased_too_many_attempts(self):
        with self.assertRaises(ThreeFailedAttempts):
            retry_purchase(item='TV', balance=100, attempts=3)

if __name__ == '__main__':
    unittest.main()