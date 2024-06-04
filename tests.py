import unittest
import sys

from dictionaries_practice import meal_1, meal_2, meal_3, title, meal_length, meal_6, translated_meal_7, key_count


class TestDictionaryProblems(unittest.TestCase):
    
  def test_meal_1(self):
    self.assertEqual("title" in meal_1, True)
    self.assertEqual("description" in meal_1, True)
    self.assertEqual("cost" in meal_1, True)

  def test_meal_2(self):
    self.assertEqual(meal_2['cost'], 12.00)

  def test_meal_3(self):
    self.assertEqual('description' in meal_3, False)

  def test_meal_4(self):
    self.assertEqual(title, "Spaghetti")

  def test_meal_5(self):
    self.assertEqual(meal_length, 3)

  def test_meal_6(self):
    self.assertDictEqual(meal_6, { "title": "Spicy Meatball Spaghetti", "description": "Pasta with some zing", "cost": 12.00 })

  def test_meal_7(self):
    self.assertEqual(translated_meal_7, "Rice with Chicken")

  def test_meal_8(self):
    self.assertEqual(key_count, 4)
