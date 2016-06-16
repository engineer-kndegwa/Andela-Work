#Defining the class as stated
########################################
#---------------------------------------------------------------
class NotesApplication(object):
	
	def __init__(self,author_name,notes_list):
		self.author_name=author_name
		self.notes_list=['One','Two','Three']
#---------------------------------------------------------------

	def create(self,note_content):
		self.note_content=note_content
		self.notes_list.append(note_content)
#---------------------------------------------------------------

	def list_content(self):
		for i in range(len(self.notes_list)):	
			return "Note ID: " + str(i) +"\n"
			return "Our Note Content: "+self.notes_list[i]+"\n"
			return "By Author: "+ self.author_name 
#---------------------------------------------------------------

	def get_note_id(self,note_id):
		self.note_id=note_id
		for i in range(len(self.notes_list)):
			if self.note_id == i:
				return "The Content for your note ID is: "+ self.notes_list[i]+"\n"
#---------------------------------------------------------------
	def search_text(self,search_text):
		self.search_text=search_text
		for notes in self.notes_list:
			if search_text==notes:
				return "\t\t\t Showing search results for " + search_text.upper()
				return "Note ID:"+ str(self.note_id)+"\n"
				return notes
				return self.author_name
#---------------------------------------------------------------
	def edit_id(self,note_id,new_content):
		self.note_id=note_id
		self.new_content=new_content
		if note_id:
			self.notes_list[note_id]=new_content
#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------

		
#Instantiating the class with an empty list
notesApp=NotesApplication("Kamau",[])
#Creating the new list item
notesApp.create("four")
#review my data
notesApp.list_content()
#get note id. the number may change accordingly i.e parameters
notesApp.get_note_id(1)
#Search text with a litte format twist as mentioned above
notesApp.search_text("One")
#EDit respective note id
#notesApp.edit_id(1,"Twenty Four")
#I have called the below method simply for the purposes of the testing the new list content
#May or may not be ommited
#notesApp.list_content()






		
