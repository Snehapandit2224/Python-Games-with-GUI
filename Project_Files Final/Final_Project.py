# Import module  
from tkinter import *
import random as r
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox
from Tic_Tac_Toe import *
from Rock_Paper_Scissors import *
from GuessTheNumber import *
#from class_CustomMessageBox import CustomMessageBox 
import sys

# Create object  
root = Tk()
root.title("Welcome!!!")
root.geometry("1200x800")
  
# Add image file 
bgd = PhotoImage(file = r"C:\Users\pandi\OneDrive\Desktop\Engineering Sem 1\CS\Mini-Project\Wall_pap.png") 
bg_image=Label(root, image=bgd)
#bg_image.place(relheight=1, relwidth=1)
bg_image.place(relheight=1, relwidth=1)

c=0#New
 
label = Label(root, text = "Which game do you want to play?", font=('Georgia',20),bg=("papaya whip"))
label.place(x=400, y=20)

b1=Button(root,padx=1,command=lambda:rock_paper_scissors(),bg="papaya whip",width=28,text="Rock Paper Scissors",font=('Georgia',18))
b1.place(x=400,y=100)

b2=Button(root,padx=1,command=lambda:Main_Program_TicTacToe(),bg="papaya whip",width=28,text="Tic Tac Toe",font=('Georgia',18))
b2.place(x=400,y=180)

b3=Button(root,padx=1,command=lambda:guess_the_number(),bg="papaya whip",width=28,text="Random Number Guessing",font=('Georgia',18))
b3.place(x=400,y=260)


root.mainloop()
