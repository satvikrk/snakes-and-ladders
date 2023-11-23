import tkinter as tk
import random
from PIL import ImageTk, Image
from win32 import win32gui
from win32 import win32con
from win32 import win32api

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
pawn=tk.Canvas(root,width=50, height=50,)
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

def movepawn(pos):
   pawn.place(x=d[pos][0], y=d[pos][1])

pos=1
def rolldice():
    global pos
    dice=random.randint(1, 6)
    pos+=dice
    movepawn(pos)
    dicelabel=tk.Label(root, text= "You rolled a "+str(dice) + "!", font=("Playfair Display",14)).place(x=1000, y=144)
#Exit Window
def close():
    win2 = tk.Tk()
    win2.geometry("350x120")
    win2.grid()
    def end():
        root.destroy()
        win2.destroy()
    def cont():
        win2.destroy()            
           
    label=tk.Label(win2, text= "Are you sure you want to exit?", font=("Playfair Display",14)).grid(column=0, row=0)
    yes=tk.Button(win2, text= "Yes", font=("Playfair Display",14), command=end, bg="#cdcdcd", fg='black').grid(column=1, row=1)
    no=tk.Button(win2, text= "No", font=("Playfair Display",14), command=cont, bg="#cdcdcd", fg='black').grid(column=2, row=1)

exit1=tk.Button(root, text= "Exit Application", font=("Playfair Display",14), command=close, bg="#a52a2a", fg='white').place(x=1000, y=44)
exit1=tk.Button(root, text= "Roll the Dice", font=("Playfair Display",14), command=rolldice, bg="#a52a2a", fg='white').place(x=1000, y=94)



root.mainloop()
