import unittest
from fizzbuzz import fizz_buzz

class FizzBuzzTest(unittest.TestCase):
	"""
	Testing the FizzBuzz
	"""
	def test_three(self):
		"""Test return fizz when input is divisible by three
		"""
		test_three=fizz_buzz(3)
		self.assertEqual(test_three,'fizz')
	def test_five(self):
		"""Test return buzz when input is divisible by five
		"""
		test_five=fizz_buzz(5)
		self.assertEqual(test_five,'buzz')
	def test_both(self):
		"""Test return fizzbuzz when input is divisible by three and five
		"""
		test_bth=fizz_buzz(15)
		self.assertEqual(test_bth,'fizzbuzz')
		
unittest.main()
