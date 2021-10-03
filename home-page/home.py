from tkinter import *
from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile


class Window(Frame):
	def __init__(self, master = None):
		Frame.__init__(self, master)
		self.master = master
		self.init_window()


	def init_window(self):
		self.master.title("GUI")
		self.pack(fill = BOTH, expand = 1)
		self.client_menu_bar()
		# self.client_buttons()
		self.client_list_box()


	def client_menu_bar(self):
		menu = Menu(self.master)
		self.master.config(menu=menu)

		# file option
		file = Menu(menu, tearoff = 0)
		file.add_command(label = "New")
		file.add_command(label = "Open", command = self.open_file)
		file.add_command(label = "Save")
		file.add_command(label = "Save As", command = self.save_as_file)
		file.add_separator()
		file.add_command(label = "Exit", command = self.client_exit)
		menu.add_cascade(label = "File", menu = file)

		#edit option
		edit = Menu(menu, tearoff = 0)
		edit.add_command(label = "Undo")
		menu.add_cascade(label = "Edit", menu = edit)

		#view option
		view = Menu(menu, tearoff = 0)
		view.add_command(label = "Window")
		menu.add_cascade(label = "View", menu = view)

		#help option
		help = Menu(menu, tearoff = 0)
		help.add_command(label = "Check for updates")
		menu.add_cascade(label = "Help", menu = help)


	def client_buttons(self):
		# intialising buttons
		btn1 = Button(self, text="1")
		btn2 = Button(self, text="2")
		btn3 = Button(self, text="3")
		btn4 = Button(self, text="4")
		btn5 = Button(self, text="5")
		btn6 = Button(self, text="6")

		# placing buttons
		btn1.place(x=10, y=30)
		btn2.place(x=30, y=30)
		btn3.place(x=50, y=30)
		btn4.place(x=10, y=60)
		btn5.place(x=30, y=60)
		btn6.place(x=50, y=60)


	def client_list_box(self):
		list_box = Listbox(self)
		list_box.pack()

		for item in ['user','from','to','how']:
			list_box.insert(END, item)



	def open_file(self):
	    file = askopenfile(mode ='r', filetypes =[('Python Files', '*.py')])
	    if file is not None:
	        content = file.read()
	        Label(self, text=content).pack()


	def save_as_file(self):
	    files = [('All Files', '*.*'),
	             ('Python Files', '*.py'),
	             ('Text Document', '*.txt')]
	    file = asksaveasfile(filetypes = files, defaultextension = files)


	# exit the application
	def client_exit(self):
		exit()


if __name__ == '__main__':
	root = Tk()
	root.geometry('500x500')
	# root.attributes('-fullscreen', True)
	app = Window(root)
	app.mainloop()
