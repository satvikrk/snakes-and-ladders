import tkinter as tk
from tkinter import *
import random
from PIL import ImageTk, Image
import time
import math

flag = True

#Initialise main window
root=tk.Tk()
root.geometry("1920x1080")
root.title("Snakes & Ladders")
root.configure(bg="#EED2CC")

#Create frame to place elements inside of
F1=tk.Frame(root, width=1000, height=1000, relief='raised')
F1.place(x=0, y=0)

#Add background image after resizing
bg=Image.open("finalboard.png")
resized_bg= bg.resize((1000,1000), Image.LANCZOS)
new_bg= ImageTk.PhotoImage(resized_bg)
bglbl=tk.Label(F1, image=new_bg)
bglbl.place(x=0, y=0)

#Player Pawn
pawn=tk.Canvas(root, width=50, height=50)
pawn.create_rectangle(0,0,100,100,fill='#039B96')
pawn.place(x=70, y=70)
  
#Index of each position
d={}
L=[[100, 99, 98, 97, 96, 95, 94, 93, 92, 91], [81, 82, 83, 84, 85, 86, 87, 88, 89, 90], [80, 79, 78, 77, 76, 75, 74, 73, 72, 71], [61, 62, 63, 64, 65, 66, 67, 68, 69, 70], [60, 59, 58, 57, 56, 55, 54, 53, 52, 51], [41, 42, 43, 44, 45, 46, 47, 48, 49, 50], [40, 39, 38, 37, 36, 35, 34, 33, 32, 31], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [20, 19, 18, 17, 16, 15, 14, 13, 12, 11], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
y=70

for i in L:
    x=70
    for j in i:
        d[j]=(x, y)
        x+=90
    y+=90

secondel=0
minuteel=0
hourel=0

def clock():
    if flag==False:
        None
    else:
        global secondel, hourel, minuteel
        if secondel==60 and minuteel==60:
            secondel=0
            minuteel=0
            hourel+=1
        elif secondel==60:
            secondel=0
            minuteel+=1
        secondelstr=str(secondel)
        minuteelstr=str(minuteel)
        hourelstr=str(hourel)

        if secondel<10:
            secondelstr="0" + str(secondel)
        if minuteel<10:
            minuteelstr="0"+ str(minuteel)
        if hourel<10:
            hourelstr="0"+ str(hourel)
            
        my_label.config(text= "Time elapsed = " + hourelstr + ":" + minuteelstr + ":" + secondelstr)
        my_label.after(1000, clock)
        secondel+=1

def update():
    my_label.config(text="New Text")

def rules():
    return None

def movepawn(pos):
    if pos<=100:
        pawn.place(x=d[pos][0], y=d[pos][1])
    if pos>100:
        pawn.place(x=d[100][0], y=d[100][1])

def rolldice():
    if flag==True:
        global pos
        dice=random.randint(1, 6)
        pos+=dice
        if pos>=100:
            win()
        movepawn(pos)
        dicelabel=tk.Label(root, text= "You rolled a "+ str(dice) + "!", font=("Playfair Display", 25, 'bold'), bg="#EED2CC").place(x=1250, y=144)
    else:
        return None

def win(): #Fix opening of multiple windows
    global flag
    if flag==True:
        import time
        end=time.time()
        win3 = tk.Tk()
        win3.title("win")
        win3.geometry("350x120")
        win3.grid()
        def close2():
            win4 = tk.Tk()
            win4.title("Exit Confirmation")
            win4.geometry("350x120")
            win4.grid()
            def end():
                win4.destroy()
                win3.destroy()
                root.destroy()
            def cont():
                win4.destroy()
            label=tk.Label(win4, text= "Are you sure you want to exit?", font=("Playfair Display", 14)).place(x=40, y=7)
            yes=tk.Button(win4, width=3, text= "Yes", font=("Playfair Display", 14), command=end, bg="#e83911", fg='#252627', activebackground="#D3FAC7", relief='flat').place(x=40, y=50)
            no=tk.Button(win4, width=3, text= "No", font=("Playfair Display", 14), command=cont, bg="#e83911", fg='#252627', activebackground="#D3FAC7", relief='flat').place(x=90, y=50)
        timetaken=end-begin
        timetaken=int(timetaken)
        labelwin=tk.Label(win3, text= "You win!", font=("Playfair Display",14)).pack()
        labeltime=tk.Label(win3, text= "Time taken: "+ str(timetaken) + "s", font=("Playfair Display",14)).pack()
        exit1=tk.Button(win3, text= "Exit Application", font=("Playfair Display",14), command=close2, bg="#e83911", fg='#252627', activebackground="#D3FAC7", relief='flat').pack()  
    else:
        return None
    flag=False

def close(): #Exit Window
    win2 = tk.Tk()
    win2.title("Exit Confirmation")
    win2.geometry("350x120")
    win2.grid()
    def end():
        win2.destroy()
        root.destroy()
    def cont():
        win2.destroy()            
           
    label=tk.Label(win2, text= "Are you sure you want to exit?", font=("Playfair Display", 14)).place(x=40, y=7)
    yes=tk.Button(win2, width=3, text= "Yes", font=("Playfair Display", 14), command=end, bg="#e83911", fg='#252627', activebackground="#D3FAC7", relief='flat').place(x=40, y=50)
    no=tk.Button(win2, width=3, text= "No", font=("Playfair Display", 14), command=cont, bg="#e83911", fg='#252627', activebackground="#D3FAC7", relief='flat').place(x=90, y=50)

my_label=Label(root, text="", font=("Playfair Display", 25, 'bold'), bg="#EED2CC", fg='#252627', activebackground="#D3FAC7", relief='flat')
my_label.place(x=1300, y=54)

clock()

begin = time.time()

pos=1
movepawn(1)

exit1=tk.Button(root, text= "Exit Application", font=("Playfair Display", 25, 'bold'), command=close, bg="#e83911", fg='#252627', activebackground="#D3FAC7", relief='flat').place(x=1000, y=44)
dice1=tk.Button(root, text= "Roll the Dice", font=("Playfair Display", 25, 'bold'), command=rolldice, bg="#e83911", fg='#252627', activebackground="#D3FAC7", relief='flat').place(x=1000, y=134)
rules1=tk.Button(root, text= "Rules", font=("Playfair Display", 25, 'bold'), command=rules, bg="#e83911", fg='#252627', activebackground="#D3FAC7", relief='flat').place(x=1000, y=224)

root.mainloop()