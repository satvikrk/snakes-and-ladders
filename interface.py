import tkinter as tk
from tkinter import *
from tkinter import ttk
import random
import time
import csv
from PIL import ImageTk, Image
import mysql.connector as m

qno=0
qL=[]
torf=False
npass=0
name=""

with open('qbank.csv', 'r') as file:
    questions=csv.reader(file)
    for i in questions:
        qL.append(i)
    qL.remove(qL[0])

flag = True
flag1 = True
ladders = {2: 38, 4: 14, 8: 30, 21: 42, 28: 76, 50: 67, 71: 92, 80: 99}
snakes = {32: 10, 34: 6, 48: 26, 62: 18, 88: 24, 95: 56, 97: 78}
pos=1

def login():
    global name
    flag=False
    import tkinter as tk
    win6=tk.Tk()
    win6.configure(bg="#EED2CC")
    win6.geometry("700x325")
    win6.grid()

    # declaring string variable
    # for storing name and password
    name_var=tk.StringVar()
    passw_var=tk.StringVar()


    # defining a function that will
    # get the name and password and 
    # print them on the screen

    def submit():
        global name
        name=name_var.get()
        print("The name is : " + name)
        name_var.set("")
        win6.destroy()
        flag=True

    def rules():
        win7=tk.Tk()
        win7.geometry("1080x350")
        win7.title("Rules")
        win7.configure(bg="#EED2CC")
        titlelbl=tk.Label(win7, wraplength=800, text= "Rules", font=("Playfair Display", 25, 'bold'), bg="#EED2CC").pack()
        with open ("rules.txt", "r") as f1:
            rulestxt=f1.read()
        ruleslbl=tk.Label(win7, wraplength=800, text= rulestxt, font=("Playfair Display", 15, 'bold'), bg="#EED2CC").pack()
    
    
    rules2 = tk.Button(win6, text= "Rules", font=("Playfair Display", 25, 'bold'), command=rules, bg="#e83911", fg='#252627', activebackground="#D3FAC7", relief='flat').place(x=100, y=170)

    def leaderboard():
        con=m.connect(host="localhost", user="root", password="root", db="satvik")
        mycursor=con.cursor()
        mycursor.execute("select * from leaderboard order by timetaken asc")
        records=mycursor.fetchall()
        recordstr=""
        for i in records:
            recordstr+=i[0]+" : "+str(i[1])+"\n"
        print(records)
        con.close()
        root1 = Tk()
        root1.geometry("500x400")
        root1.title("Leaderboard")
        root1.configure(bg="#EED2CC")

        main_frame = Frame(root1)
        main_frame.pack(fill=BOTH, expand=1)

        my_canvas = Canvas(main_frame)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.configure(bg="#EED2CC")
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

        second_frame = Frame(my_canvas)
        second_frame.configure(bg="#EED2CC")

        my_canvas.create_window((0,0), window=second_frame, anchor="nw")

        my_label = Label(second_frame, text=recordstr, font=("Playfair Display", 18, 'bold'), bg="#EED2CC").pack()

        root1.mainloop()

    name_label = tk.Label(win6, text = 'Username', font=("Playfair Display", 15, 'bold'))
    name_entry = tk.Entry(win6, textvariable = name_var, font=("Playfair Display", 27, 'bold'))

    sub_btn=tk.Button(win6, text= "→", font=("Playfair Display", 18, 'bold'), command=submit, bg="#D3FAC7", fg='#252627', activebackground="#e83911", relief='flat', pady=0).place(x=550, y=100)
    ldb_btn=tk.Button(win6, text= "Leaderboard", font=("Playfair Display", 25, 'bold'), command=leaderboard, bg="#e83911", fg='#252627', activebackground="#D3FAC7", relief='flat').place(x=225, y=170)

    name_label.place(x=100, y=50)
    name_entry.place(x=100, y=100)
    win6.mainloop()

login()


def fn():
    global pos
    global npass
    flag1=False
    win5 = tk.Tk()
    win5.title("Exit Confirmation")
    win5.geometry("1080x720")

    def disable_event():
        pass

    win5.protocol("WM_DELETE_WINDOW", disable_event)

    def question():
        global qno
        x=len(qL)
        qno=random.randint(0, x-1)
        q=qL[qno][1]
        my_label=Label(win5, text=q, wraplength=500, font=("Playfair Display", 18, 'bold'), bg="#FFFFFF", fg='#252627', activebackground="#D3FAC7", relief='flat').pack()
        return True

    def pass1():
        global npass
        global torf
        npass+=1
        torf=False
        movepawn2()
        win5.destroy()

    def pass2():
        win5.destroy()

    tk.Label(win5, text= "Question:", font=("Playfair Display", 14)).pack()
    question()
    pass_btn=tk.Button(win5, width=3, text= "Pass", font=("Playfair Display", 14), command=pass1, bg="#e83911", fg='#252627', activebackground="#D3FAC7", relief='flat').pack() 

    def movepawn2():
        global pos
        if pos in snakes:
            if not torf:
                l1=Label(root, width=60, text="The snake at position "+str(pos)+" has bitten you. Your current position is "+ str(snakes[pos])+".", font=("Playfair Display", 19, 'bold'), bg="#FFFFFF", fg='#252627', activebackground="#D3FAC7", relief='flat')
                l1.place(x=1000, y=314)
                pos=snakes[pos]
                pawn.place(x=d[pos][0], y=d[pos][1])
            else:
                pawn.place(x=d[pos][0], y=d[pos][1])
        elif pos in ladders:
            if torf:
                l2=Label(root, width=60, text="You have climbed up the ladder at position "+str(pos)+". Your current position is "+ str(ladders[pos])+".", font=("Playfair Display", 18, 'bold'), bg="#FFFFFF", fg='#252627', activebackground="#D3FAC7", relief='flat')
                l2.place(x=1000, y=314)
                pos=ladders[pos]
                pawn.place(x=d[pos][0], y=d[pos][1])
            else:
                pawn.place(x=d[pos][0], y=d[pos][1])

    def submit():
        global npass
        global torf
        answer = textBox.get("1.0", "end-1c")
        print(answer)
        if " "+answer.lower() in qL[qno][2:]:
            torf = True
        else:
            torf = False
            npass+=1
        movepawn2()
        win5.destroy()
    
    textBox = Text(win5, font=("Playfair Display", 14), height = 2, width = 15)
    textBox.pack()
    tk.Button(win5, text = 'Submit', command = lambda:submit()).pack()

    flag1=True
    return torf

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
    global flag
    if flag==True:
        win6=tk.Tk()
        win6.geometry("1080x350")
        win6.title("Rules")
        win6.configure(bg="#EED2CC")
        titlelbl=tk.Label(win6, wraplength=800, text= "Rules", font=("Playfair Display", 25, 'bold'), bg="#EED2CC").pack()
        with open ("rules.txt", "r") as f1:
            rulestxt=f1.read()
        ruleslbl=tk.Label(win6, wraplength=800, text= rulestxt, font=("Playfair Display", 15, 'bold'), bg="#EED2CC").pack()

def leaderboard():
    con=m.connect(host="localhost", user="root", password="root", db="satvik")
    mycursor=con.cursor()
    mycursor.execute("select * from leaderboard order by timetaken asc")
    records=mycursor.fetchall()
    recordstr=""
    for i in records:
        recordstr+=i[0]+" : "+str(i[1])+"\n"
    print(records)
    con.close()
    root1 = Tk()
    root1.geometry("500x400")
    root1.title("Leaderboard")
    root1.configure(bg="#EED2CC")

    main_frame = Frame(root1)
    main_frame.pack(fill=BOTH, expand=1)

    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.configure(bg="#EED2CC")
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

    second_frame = Frame(my_canvas)
    second_frame.configure(bg="#EED2CC")

    my_canvas.create_window((0,0), window=second_frame, anchor="nw")

    my_label = Label(second_frame, text=recordstr, font=("Playfair Display", 18, 'bold'), bg="#EED2CC").pack()

    root1.mainloop()

def movepawn():
    global pos
    if flag==True:
        if pos<=100:
            pawn.place(x=d[pos][0], y=d[pos][1])
        elif pos>100:
            pawn.place(x=d[100][0], y=d[100][1])
    else:
        return None

def rolldice():
    if flag==True and flag1==True:
        global pos
        dice = random.randint(1, 6)
        pos+=dice
        if pos>=100:
            win()
        elif pos in snakes:
            fn()
        elif pos in ladders:
            fn()
        else:
            movepawn()
        dicelabel=tk.Label(root, text= "You rolled a "+ str(dice) + "!", font=("Playfair Display", 25, 'bold'), bg="#EED2CC").place(x=1250, y=144)
    else:
        return None

def win(): #Fix opening of multiple windows
    global name
    global flag
    global npass
    if flag==True:
        import time
        end=time.time()
        win3 = tk.Tk()
        win3.title("win")
        win3.geometry("500x200")
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
        timetaken= end-begin
        timetaken=int(timetaken) + (npass*20)
        with open("Leaderboard.txt", "a") as f5:
            entry=name + " : " + str(timetaken) + "\n"
            f5.write(entry)
        labelwin=tk.Label(win3, text= "You win!", font=("Playfair Display",14)).pack()
        labelnpass=tk.Label(win3, text= "Number of passes and incorrect answers="+str(npass), font=("Playfair Display",14)).pack()
        labeltime=tk.Label(win3, text= "Time taken: "+ str(timetaken) + "s", font=("Playfair Display",14)).pack()
        exit1=tk.Button(win3, text= "Exit Application", font=("Playfair Display",14), command=close2, bg="#e83911", fg='#252627', activebackground="#D3FAC7", relief='flat').pack()  
    else:
        return None
    flag=False
    leaderboard()

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

exit1 = tk.Button(root, text= "Exit Application", font=("Playfair Display", 25, 'bold'), command=close, bg="#e83911", fg='#252627', activebackground="#D3FAC7", relief='flat').place(x=1000, y=44)
dice1 = tk.Button(root, text= "Roll the Dice", font=("Playfair Display", 25, 'bold'), command=rolldice, bg="#e83911", fg='#252627', activebackground="#D3FAC7", relief='flat').place(x=1000, y=134)
rules1 = tk.Button(root, text= "Rules", font=("Playfair Display", 25, 'bold'), command=rules, bg="#e83911", fg='#252627', activebackground="#D3FAC7", relief='flat').place(x=1000, y=224)

root.mainloop()