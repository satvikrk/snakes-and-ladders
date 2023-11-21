import tkinter as tk
from PIL import ImageTk, Image

root=tk.Tk()
root.geometry("1920x1080")
root.title("Snakes & Ladders")

F1=tk.Frame(root, width=1000, height=1000, relief='raised')
F1.place(x=0, y=0)

bg=Image.open("finalboard.png")
resized_bg= bg.resize((1000,1000), Image.LANCZOS)
new_bg= ImageTk.PhotoImage(resized_bg)
bglbl=tk.Label(F1, image=new_bg)
bglbl.place(x=0, y=0)

b1=tk.Button(root, text="Rules", height=3, width=20, fg="#BABABA", bg="#EEEEEE", font=("Poppins", "14", "bold"), relief="flat")
b1.place(x=1200, y=400)

root.mainloop()