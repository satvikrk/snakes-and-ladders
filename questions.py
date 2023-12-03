import tkinter as tk
from tkinter import *
import random
import time
import csv
from PIL import ImageTk,Image


qno=0
qL=[]
torf=False

with open('qbank.csv', 'r') as file:
    questions=csv.reader(file)
    for i in questions:
        qL.append(i)
    qL.remove(qL[0])

def fn():

    win5 = tk.Tk()
    win5.title("Exit Confirmation")
    win5.geometry("1080x720")

    def question():
        global qno
        x=len(qL)
        qno=random.randint(0, x-1)
        q=qL[qno][1]
        my_label=Label(win5, text=q, font=("Playfair Display", 18, 'bold'), bg="#FFFFFF", fg='#252627', activebackground="#D3FAC7", relief='flat').pack()
        return True

    def pass1():
        time.sleep(5)
        win5.destroy()

    def pass2():
        win5.destroy()

    question()

    tk.Label(win5, text= "Question:", font=("Playfair Display", 14)).pack()
    pass_btn=tk.Button(win5, width=3, text= "Pass", font=("Playfair Display", 14), command=pass1, bg="#e83911", fg='#252627', activebackground="#D3FAC7", relief='flat').pack() 


    def submit():
        global torf
        answer = textBox.get("1.0", "end-1c")
        if " "+answer.lower() in qL[qno][2:]:
            torf = True
        else:
            torf = False
        win5.destroy()
    
    textBox = Text(win5, font=("Playfair Display", 14), height = 2, width = 15)
    textBox.place(x = 200, y = 155)
    tk.Button(win5, text = 'Submit', command = lambda:submit()).pack()

    return torf