

from tkinter import *
from tkinter import messagebox
from class_CustomMessageBox import CustomMessageBox#<--->
import random
import sys
import time#"New"

# functions
def guess_the_number():
   global root2
   global i
   root2=Tk()
   #root2=Toplevel()
   root2.title("GUESS THE NUMBER")
   root2.geometry("1000x700")

   s_no = "none"

   i=3

   # functions

   def StartGame():
      global s_no

      for button in button_list:

      
        randomButton = random.choice(button_list)
        button.config(text=str(random.randint(1,16)))
        s_no = randomButton.cget("text")

   def continue_game():#----->
       message_box = CustomMessageBox('Do you want to play again?', 'Do you want to play again?', 'Yes', 'No',root2)
       if(message_box.choice=="Yes"):
          
         answer_label.config(text=("Start"))
       else:
            root2.withdraw()
           #root2.destroy()
           #time.sleep(2)#"New"
           #sys.exit()#--->


   def OnClick(event):
           global i
           global s_no
           if(i>1):
                   i-=1
   #        for i in range(1,4):  #--->
                   btn = event.widget
                   buttonText = btn.cget("text")
                   if s_no==buttonText:
                           answer_label.config(text=("You won"+" The secret number is:"+s_no))
                           time.sleep(2)
                           StartGame()#--->
                           continue_game()#--->
   #                        break
                   else:
                           answer_label.config(text=("Your guess is wrong! Try again, Tries left: "+str(i)))#--->
           else:
                   
                   answer_label.config(text=("You Lose!"+"The secret number is:"+s_no))#"New"
                   #time.sleep(2)#"New"
                   StartGame()#--->
                   continue_game()#--->
                   i=3
                   

   # gui components

   title_label = Label(root2, text="Guess the number!!!", font=("Helvetical 16"),pady=30, justify="center")
   button_one = Button(root2, text="00", font=("Helvetical 15"), width=20, pady=40, bg="burlywood1")
   button_two = Button(root2, text="00", font=("Helvetical 15"), width=20, pady=40, bg="burlywood2")
   button_three = Button(root2, text="00", font=("Helvetical 15"), width=20, pady=40, bg="burlywood3")
   button_four = Button(root2, text="00", font=("Helvetical 15"), width=20, pady=40, bg="burlywood4")
   button_five = Button(root2, text="00", font=("Helvetical 15"), width=20, pady=40, bg="burlywood2")
   button_six = Button(root2, text="00", font=("Helvetical 15"), width=20, pady=40, bg="burlywood3")
   button_seven = Button(root2, text="00", font=("Helvetical 15"), width=20, pady=40, bg="burlywood4")
   button_eight = Button(root2, text="00", font=("Helvetical 15"), width=20, pady=40, bg="burlywood1")
   button_nine = Button(root2, text="00", font=("Helvetical 15"), width=20, pady=40, bg="burlywood3")
   button_ten = Button(root2, text="00", font=("Helvetical 15"), width=20, pady=40, bg="burlywood4")
   button_eleven = Button(root2, text="00", font=("Helvetical 15"), width=20, pady=40, bg="burlywood1")
   button_twelve = Button(root2, text="00", font=("Helvetical 15"), width=20, pady=40, bg="burlywood2")
   button_thirteen = Button(root2, text="00", font=("Helvetical 15"), width=20, pady=40, bg="burlywood4")
   button_fourteen = Button(root2, text="00", font=("Helvetical 15"), width=20, pady=40, bg="burlywood1")
   button_fifteen = Button(root2, text="00", font=("Helvetical 15"), width=20, pady=40, bg="burlywood2")
   button_sixteen = Button(root2, text="00", font=("Helvetical 15"), width=20, pady=40, bg="burlywood3")

   button_list = [button_one, button_two, button_three, button_four, button_five, button_six, button_seven, button_eight, button_nine, button_ten, button_eleven, button_twelve, button_thirteen, button_fourteen, button_fifteen, button_sixteen]

   answer_label = Label(root2, text="choose any number", font=("Helvetical 15"), width=50, pady=20, fg="black", bg="grey", justify="center")#width--->

   title_label.grid(row=0, column=1)
#title_label.grid(row=0, column=0, columnspan=3)
   button_one.grid(row=1, column=0)
   button_two.grid(row=1, column=1)
   button_three.grid(row=1, column=2)
   button_four.grid(row=1, column=3)
   button_five.grid(row=2, column=0)
   button_six.grid(row=2, column=1)
   button_seven.grid(row=2, column=2)
   button_eight.grid(row=2, column=3)
   button_nine.grid(row=3, column=0)
   button_ten.grid(row=3, column=1)
   button_eleven.grid(row=3, column=2)
   button_twelve.grid(row=3, column=3)
   button_thirteen.grid(row=4, column=0)
   button_fourteen.grid(row=4, column=1)
   button_fifteen.grid(row=4, column=2)
   button_sixteen.grid(row=4, column=3)



   answer_label.grid(row=6, column=0, columnspan=5)

   button_one.bind("<Button-1>", OnClick)
   button_two.bind("<Button-1>", OnClick)
   button_three.bind("<Button-1>", OnClick)
   button_four.bind("<Button-1>", OnClick)
   button_five.bind("<Button-1>", OnClick)
   button_six.bind("<Button-1>", OnClick)
   button_seven.bind("<Button-1>", OnClick)
   button_eight.bind("<Button-1>", OnClick)
   button_nine.bind("<Button-1>", OnClick)
   button_ten.bind("<Button-1>", OnClick)
   button_eleven.bind("<Button-1>", OnClick)
   button_twelve.bind("<Button-1>", OnClick)
   button_thirteen.bind("<Button-1>", OnClick)
   button_fourteen.bind("<Button-1>", OnClick)
   button_fifteen.bind("<Button-1>", OnClick)
   button_sixteen.bind("<Button-1>", OnClick)

   StartGame()

   root2.mainloop()




       
