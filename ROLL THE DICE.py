from tkinter import* 
import random
root=Tk()
root.geometry("1000x600")
root.title("ROLL THE DICE")
label = Label (root, text="", font = ("times",260))
def roll():
 dice=['\u2680', '\u2681', '\u2682', '\u2683', '\u2684','\u2685']
 label.configure(text=f'{random.choice(dice)}{random.choice(dice)}')
 label.pack()

button=Button(root,text="ROLL THE DICE",width=50,height=5,font=50,bg="RED", 
              bd=20,command=roll)

button.pack(padx=10, pady=10)

root.mainloop()