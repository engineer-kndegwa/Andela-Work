import unittest
from notesapplication import NotesApplication

class TestNotesApp(unittest.TestCase):
	def test_single_note(self):
		"""Test that a single note is stored properly"""
		test_notesApp = NotesApplication(')
		test_notesApp.create('Four')
		self.assertIn('Four',test_notesApp.notes_list)
	
unittest.main()
