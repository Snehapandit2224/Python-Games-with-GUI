import random as r
from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
import sys
import time
from class_CustomMessageBox import CustomMessageBox #

def rock_paper_scissors():
    def won():
        messagebox.showinfo('You Won!! :D','''
Congrats!!!
You won!!!
Computer chose: '''+c)

    def lost():

        messagebox.showinfo('You Lost :( ','Oops!! '+c+" has won")

    def tie():

        messagebox.showinfo('Its a Tie!','''
You tied!
Play again to win!!

Computer chose:'''+c)

    def play_box():
        global d
        message_box = CustomMessageBox('Do you want to play again?', 'Do you want to play again?', 'Yes', 'No',win)
        if(message_box.choice=="Yes"):
            rock_paper_scissors#<--->
        else:
            #win.destroy()
            win.withdraw()
            #sys.exit()#--->

    def play_box_no():

        messagebox.showinfo('''
        Thanks for playing!!!
        We enjoyed playing with you :)
    ''')

    global c#New
        
    win = Toplevel()
    win.geometry("350x200")
    win.config(bg='darkturquoise')
    a="" 
    d=0
    def choice_selection():
        global a
        a=str(radio.get())
        print(radio.get())
        selected = "You selected the option " + a
        label.config(text=selected,bg='darkturquoise')
        print('C: ',c)
        if(a!=""):
            check=False#
            if a.lower()==c: 
                tie()
                check=True#
                time.sleep(1)#NewNew
                play_box()
            elif (a.lower()=='rock' and c.lower()=='paper')or(a.lower()=='paper' and c.lower()=='scissors')or(a.lower()=='scissors' and c.lower()=='rock'):
                lost()
                check=True#
                time.sleep(1)#NewNew
                play_box()#
            elif (a.lower()=='rock' and c.lower()=='scissors')or(a.lower()=='paper' and c.lower()=='rock')or(a.lower()=='scissors' and c.lower()=='paper'):
                won()
                check=True#
                time.sleep(1)#NewNew
                play_box()#
            if(check): #
                if d==2:
                    play_box_no()
                    #win.destroy()#
                    win.withdraw()
            
    radio = StringVar()
    Label(win,text="Choose rock paper or scissors:", font=('Aerial 11'),bg='white').pack() #added win here
    r1 = Radiobutton(win, text="Rock", variable=radio,value="Rock",font=('Aerial 11'),bg='white',command=choice_selection)
    r2 = Radiobutton(win, text="Paper", variable=radio,value="Paper",font=('Aerial 11'), command=choice_selection,bg='white')
    r3 = Radiobutton(win, text="Scissors", variable=radio, value="Scissors",font=('Aerial 11'), command=choice_selection,bg='white')
    r1.pack(anchor=N)
    r2.pack(anchor=N)
    r3.pack(anchor=N)
    label = Label(win)
    label.pack()
    
    b=['rock','paper','scissors']
    c=r.choice(b)

    win.mainloop()
#rock_paper_scissors()

