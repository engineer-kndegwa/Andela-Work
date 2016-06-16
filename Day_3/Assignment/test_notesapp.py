import unittest
from notesapplication import NotesApplication

class TestNotesApp(unittest.TestCase):
	"""Beginning the test methods"""
	def test_single_note(self):
		"""Test that a single note is stored properly"""
		test_notesApp = NotesApplication('')
		test_notesApp.create('Four')
		self.assertIn('Four',test_notesApp.notes_list)
	def test_if_note_id_is_an_integer(self):
		"""Testing if the note id is indeed not an integer"""
		test_if_int = NotesApplication('')
		concl = test_if_int.get_note_id(1)
		self.assertEqual(type(concl),int)
		"""This is an expected failure because it was type cast to a string"""
	def test_list_content_not_empty(self):
		"""This tests if the notes_list is empty or not"""
		test_if_content= NotesApplication('Dummy Content')
		test_list_content_if_empty = test_if_content.list_content()
		self.assertEqual(test_list_content_if_empty, None)
	
	
unittest.main()
