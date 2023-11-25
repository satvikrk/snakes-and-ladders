from tkinter import *
import time

'''
#hourini = int(time.strftime("%H"))
#minuteini = int(time.strftime("%M"))
secondini = int(time.strftime("%S"))    
hourel=0
minuteel=0

root=Tk()
root.title("stopwatch")
root.geometry("600x400")

def clock():
    global hourel, minuteel
    #hour = int(time.strftime("%H"))
    #minute = int(time.strftime("%M"))
    second = int(time.strftime("%S"))
    secondel=second-secondini
    if secondel<0:
        secondel+=60
    if minuteel==60 and secondel==60:
        hourel+=1
        secondel=0
        minuteel=0
    if secondel==60:
        minuteel=minuteel + 1
        secondel=0
    if minuteel==60:
        hourel+=1
        minuteel=0
    my_label.config(text=str(hourel) + ":" + str(minuteel) + ":" + str(secondel))
    my_label.after(1000, clock)'''


secondel=0
minuteel=0
hourel=0

root=Tk()
root.title("stopwatch")
root.geometry("600x400")

def clock():
    global secondel, hourel, minuteel
    secondel+=1
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
        
    my_label.config(text= hourelstr + ":" + minuteelstr + ":" + secondelstr)
    my_label.after(1000, clock)

def update():
    my_label.config(text="New Text")

my_label=Label(root, height=1, width=8, text="", font=("Helvetica", 48), fg='white', bg='black')
my_label.pack(pady=20)

clock()

root.mainloop()

