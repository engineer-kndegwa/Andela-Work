import unittest
from notesapplication import NotesApplication

class TestNotesApp(unittest.TestCase):
	"""Beginning the test methods"""
	def test_single_note(self):
		"""Test that a single note is stored properly"""
		test_notesApp = NotesApplication('',[])
		test_notesApp.create('Four')
		self.assertIn('Four',test_notesApp.notes_list)
	def test_author_name_if_string(self):
		"""Testing if name is a string"""
		exampleClass = NotesApplication('Kunene',[])
		self.assertEqual(type(exampleClass.author_name),str)
	def test_if_author_name_is_in_existence_when_object_is_instantiated(self):
		"""Testing if name is accessible"""
		exampleClass2 = NotesApplication('Kunene',[])
		self.assertEqual(exampleClass2.author_name,'Kunene')
	def test_if_author_name_is_not_an_integer_explicitly(self):
		'''Explicit test to conirm that the author name is not an integer Explicitly'''
		exampleClass3 = NotesApplication('Wambugu',[])
		self.assertNotEqual(type(exampleClass3.author_name),int)
	def test_note_instance(self):
		exampleClass4 = NotesApplication('WALALO',['This is my fifth note probably'])
		self.assertIsInstance(exampleClass4, NotesApplication, msg='The object should be an instance of the `NotesApplication class')
	def test_object_type(self):
		exampleclass5 = NotesApplication('This is my sixth note',[])
		self.assertTrue((type(exampleclass5) is NotesApplication), msg='The object should be a type of `NotesApplication`')
								
	def test_if_note_id_is_an_integer(self):
		"""Testing if the note id is indeed not an integer"""
		test_if_int = NotesApplication('',[])
		concl = test_if_int.get_note_id(1)
		self.assertEqual(type(concl),str)
		"""This is an expected failure because it was type cast to a string"""
	def test_list_content_not_empty(self):
		"""This tests if the notes_list is empty or not"""
		test_if_content= NotesApplication('Dummy Content',[])
		test_list_content_if_empty = test_if_content.list_content()
		self.assertEqual(test_list_content_if_empty, None)
	
	
unittest.main()
