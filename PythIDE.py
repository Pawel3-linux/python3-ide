# C++ IDE
from tkinter import *
from tkinter import messagebox
import os
class Application(Frame):
	def __init__(self, master):
		super(Application, self).__init__(master)
		self.grid()
		self.create_widgets()

	def compilegpp(self):
		test = os.system("g++ " + self.namebefore.get() + " -o " + self.nameafter.get())
		if test != 0:
			messagebox.showerror(title = "Error", message = "Compilation failed.")
		else:
			messagebox.showinfo(title = "Compilation", message = "Compilation ended successfully.")
	def run(self):
		with open('runner.sh', 'w') as f:
			f.write("\n" + self.nameafter.get() + "\necho \"Running program done, press Enter to continue...\"\nread _\n")
		os.system('chmod +x runner.sh')
		os.system('x-terminal-emulator -e ./runner.sh')

	def endide(self):
		exit()
	def save(self):
		with open(self.namebefore.get(), 'w') as file_: print(self.edit.get(0.0, END), file=file_)

	def create_widgets(self):
		self.edit = Text(self, width = 45, height = 30, wrap = WORD)
		self.namebefore_text = Label(self, text = "Name of file to save and compile (full path):")
		self.namebefore = Entry(self)
		self.nameafter_text = Label(self, text = "Name of file to create (full path):")
		self.nameafter = Entry(self)
		self.save_button = Button(self, text = "Only Save", command = self.save)
		self.comp_button = Button(self, text = "Compile (g++)", command = self.compilegpp)
		self.run_button = Button(self, text = "Run", command = self.run)
		self.close_button = Button(self, text = "Close IDE", command = self.endide)
		self.edit.grid(row = 0, column = 0, sticky = W)
		self.namebefore_text.grid(row = 1, column = 0, sticky = W)
		self.namebefore.grid(row = 1, column = 1, sticky = W)
		self.nameafter_text.grid(row = 2, column = 0, sticky = W)
		self.nameafter.grid(row = 2, column = 1, sticky = W)
		self.comp_button.grid(row = 0, column = 2, sticky = W)
		self.run_button.grid(row = 0, column = 3, sticky = W)
		self.save_button.grid(row = 0, column = 4, sticky = W)
		self.close_button.grid(row = 0, column = 5, sticky = W)

root = Tk()
root.title("C++ IDE")
root.geometry("1000x700")

app = Application(root)
root.mainloop()
