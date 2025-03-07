from tkinter import *
from tkinter import messagebox
class CustomMessageBox:
    def __init__(self, title, message, button1_text, button2_text,parent):
        self.title = title
        self.message = message
        self.button1_text = button1_text
        self.button2_text = button2_text
        self.choice = None

        self.root = Toplevel(parent)
        self.root.withdraw()

        result = messagebox.askquestion(self.title, self.message, icon='warning', master=parent)
        if result == 'yes':
            self.choice = self.button1_text
        else:
            self.choice = self.button2_text
    

    

        
