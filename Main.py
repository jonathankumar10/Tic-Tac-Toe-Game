from tkinter import *


root = Tk()

canvas = Canvas(root)
canvas.pack()

frame = Frame(canvas)
frame.pack()

root.title("Tic Tac Toe")

title = Label(frame, text="Tic Tac Toe", justify=CENTER, font="times 25")
title.grid(row=0,column=2)

name1 = Label(frame, text="Player 1 : X", font="times 20")
name1.grid(row=1,column=1)

name2 = Label(frame, text="Player 2 : 0", font="times 20")
name2.grid(row=2,column=1)

space1 = Label(frame, text="      ", font="times 20")
space1.grid(row=1,column=2)

space2 = Label(frame, text="      ", font="times 20")
space2.grid(row=2,column=2)

newGame = Label(frame, text="New Game", font="times 20")
newGame.grid(row=1,column=3)

resetGame = Label(frame, text="Reset game", font="times 20")
resetGame.grid(row=2,column=3)

b1 = Button(frame, width = 20, height = 10)
b1.grid(row=3,column=1)

b2 = Button(frame, width = 20, height = 10)
b2.grid(row=3,column=2)

b3 = Button(frame, width = 20, height = 10)
b3.grid(row=3,column=3)

b4 = Button(frame, width = 20, height = 10)
b4.grid(row=4,column=1)

b5 = Button(frame, width = 20, height = 10)
b5.grid(row=4,column=2)

b6 = Button(frame, width = 20, height = 10)
b6.grid(row=4,column=3)

b7 = Button(frame, width = 20, height = 10)
b7.grid(row=5,column=1)

b8 = Button(frame, width = 20, height = 10)
b8.grid(row=5,column=2)

b9 = Button(frame, width = 20, height = 10)
b9.grid(row=5,column=3)

root.mainloop()