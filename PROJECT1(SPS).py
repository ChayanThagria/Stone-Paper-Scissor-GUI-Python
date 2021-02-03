import random
from tkinter import *

#basic interface
root = Tk()
root.geometry("600x400")
root.maxsize(600,400)
root.title("Stone Paper Scissor-chayan")
title_label = Label(text = "Stone-Paper-Scissor",font = "Times 30 bold italic",fg = "maroon")
title_label.pack(side = TOP)
instruction_img = PhotoImage(file = r"instructions.png")
instruction_img_main = instruction_img.subsample(13,13)
f1 = Frame(root,borderwidth = 100,bg = "white")
f1.pack(side = LEFT,fill = X)
instruction_label = Label(f1,text = "Choose!!",font = "Comicsansms 20 italic",bg = "white",image = instruction_img_main)
instruction_label.pack(side = TOP)
#variables
user_input = StringVar()
u=[]
c =[]
#logic
computer_input = random.choice(["stone", "paper", "scissor"])

#Button Functions


def stone():

    user_input = "stone"


    if computer_input == "paper":
        scvalue.set(f"lose computer choose {computer_input}")
        screen.update()
        c.append(1)
        computer_score.set(f"computer score - {str(sum(u))}")
        screen2.update()


    elif computer_input == "scissor":
        scvalue.set(f"win computer choose {computer_input}")
        screen.update()
        u.append(1)
        user_score.set(f"user score - {str(sum(u))}")
        screen1.update()

    else:
        scvalue.set("draw")

def paper():

    user_input = "paper"


    if computer_input == "stone":
        scvalue.set(f"win computer choose {computer_input}")
        screen.update()
        u.append(1)
        user_score.set(f"user score - {str(sum(u))}")
        screen1.update()

    elif computer_input == "scissor":
        scvalue.set(f"lose computer choose {computer_input}")
        screen.update()
        c.append(1)
        computer_score.set(f"computer score - {str(sum(u))}")
        screen2.update()
    else:
        scvalue.set("draw")

def scissor():

    user_input = "scissor"


    if computer_input == "stone":
        scvalue.set(f"lose computer choose {computer_input}")
        screen.update()
        c.append(1)
        computer_score.set(f"computer score - {str(sum(u))}")
        screen2.update()

    elif computer_input == "paper":
        scvalue.set(f"win computer choose {computer_input}")
        screen.update()
        u.append(1)
        user_score.set(f"user score - {str(sum(u))}")
        screen1.update()

    else:
        scvalue.set("draw")


#result screen
scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 10 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)
screen.update()

#user result screen
user_score=StringVar()
user_score.set(f"user score - {str(sum(u))}")
screen1 = Entry(root, textvar=user_score, font="lucida 10 bold")
screen1.pack(fill=X, ipadx=8, pady=10, padx=10)
screen1.update()

#computer result screen
computer_score=StringVar()
computer_score.set(f"computer score - {str(sum(c))}")
screen2 = Entry(root, textvar=computer_score, font="lucida 10 bold")
screen2.pack(fill=X, ipadx=8, pady=10, padx=10)
screen2.update()

#buttons
f3 = Frame(root)
f3.pack(side = RIGHT,fill = X)

img_stone = PhotoImage(file = r"rock.png")
img_stone_main = img_stone.subsample(6,6)
b1 = Button(f3,text = "STONE",font = "Comicsansms 20 italic",command = stone,image = img_stone_main)
b1.pack(side = LEFT)

img_paper = PhotoImage(file = r"paper.png")
img_paper_main = img_paper.subsample(6,6)
b2 = Button(f3,text = "PAPER",font = "Comicsansms 20 italic",command =paper,image = img_paper_main)
b2.pack(side = LEFT)

img_scissor = PhotoImage(file = r"scissor.png")
img_scissor_main = img_scissor.subsample(6,6)
b3 = Button(f3,text = "SCISSOR",font = "Comicsansms 20 italic",command =scissor,image = img_scissor_main)
b3.pack(side = LEFT)

print("Thank You for playing")
root.mainloop()

