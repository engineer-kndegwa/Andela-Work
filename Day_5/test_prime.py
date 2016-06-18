import unittest
from isprime import isPrime

class TestPrime(unittest.TestCase):
	'''Testing my prime numbers module'''
	def test_if_result_is_string(self):
		"""Checking if the result submitted is a string"""
		test1 = isPrime(10)
		self.assertEqual(type(test1),list)
	def test_if_number_input_is_what_is_gotten(self):
		"""if i want the first 15 numbers do i get 10 numbers is my list"""
		test2 = isPrime(15)
		self.assertEqual(len(test2),15)
	def test_if_list_exists(self):
		"""Sure check to ensure the list with the prime numbers exists"""
		test3 = isPrime(5)
		self.assertIsNotNone(test3)
	def test_if_list_exists_when_zero_passed(self):
		"""This test should be failed because no argument is passed thus in application"""
		test4 = isPrime()
		self.assertIsNone(test4)
	def test_2_is_always_part_of_result(self):
		test5 = isPrime(5)
		self.assertIn(test5,2)
		


unittest.main()
