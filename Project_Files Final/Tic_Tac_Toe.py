
from tkinter import *
from tkinter import messagebox
import random as r
from class_CustomMessageBox import CustomMessageBox#<--->
import sys

def Main_Program_TicTacToe():
    def button(frame):          #Function to define a button
        b=Button(frame,padx=1,bg="black",width=3,text="   ",font=('arial',60,'bold'),relief="sunken",bd=10)
        return b
    def change_a():             #Function to change the operand for the next player
        global a
        for i in ['O','X']:
            if not(i==a):
                a=i
                break
    def reset():                #Resets the game
        global a
        for i in range(3):
            for j in range(3):
                    b[i][j]["text"]=" "
                    b[i][j]["state"]=NORMAL
        a=r.choice(['O','X'])

    
    def continue_game():
        message_box = CustomMessageBox('Do you want to play again?', 'Do you want to play again?', 'Yes', 'No',root1)
        if(message_box.choice=="Yes"):
    
            Main_Program_TicTacToe#<--->
        else:
            root1.withdraw()
            #root1.destroy()
            #sys.exit()#--->
    
    def check():                #Checks for victory or Draw
        for i in range(3):
                if(b[i][0]["text"]==b[i][1]["text"]==b[i][2]["text"]==a or b[0][i]["text"]==b[1][i]["text"]==b[2][i]["text"]==a):
                        messagebox.showinfo("Congrats!!","'"+a+"' has won", master=root1)
                        reset()
                        continue_game()
        if(b[0][0]["text"]==b[1][1]["text"]==b[2][2]["text"]==a or b[0][2]["text"]==b[1][1]["text"]==b[2][0]["text"]==a):
            messagebox.showinfo("Congrats!!","'"+a+"' has won",master=root1)
            reset()
            continue_game()
        elif(b[0][0]["state"]==b[0][1]["state"]==b[0][2]["state"]==b[1][0]["state"]==b[1][1]["state"]==b[1][2]["state"]==b[2][0]["state"]==b[2][1]["state"]==b[2][2]["state"]==DISABLED):
            messagebox.showinfo("Tied!!","The match ended in a draw")
            reset()
            continue_game()
    def click(row,col):
            b[row][col].config(text=a,state=DISABLED,disabledforeground=colour[a])
            check()
            change_a()
            label.config(text=a+"'s Chance")

###############   Main Program #################

#def Main_Program_TicTacToe():#<--->
    global label
    global a
    global colour
    global b
    global root1
    root1=Tk()                   #Window defined
    #root1=Toplevel()
    root1.title("Tic-Tac-Toe")   #Title given
    a=r.choice(['O','X'])       #Two operators defined
    colour={'O':"white",'X':"white"}
    b=[[],[],[]]
    def play():#--->
        for i in range(3):
            for j in range(3):
                b[i].append(button(root1))
                b[i][j].config(command= lambda row=i,col=j:click(row,col))
                b[i][j].grid(row=i,column=j)
    play()#---->
    label=Label(root1,text=a+"'s Chance",font=('arial',20,'bold'))#root1 is extra
    label.grid(row=3,column=0,columnspan=3)    
    root1.mainloop()
#Main_Program_TicTacToe()
