import unittest
from fizzbuzz import fizz_buzz

class FizzBuzzTest(unittest.Testcase):
	"""
	Testing the FizzBuzz
	"""
	def test_three(self):
		"""Test return Fizz when input is divisible by three
		"""
		test_three=fizz_buzz(3)
		self.assertEqual(test_three,'Fizz')
		
