from tkinter import *

root = Tk()

name1 = Label(root, text="Player 1 : X", font="times 20")
name1.grid(row=0,column=1)

name2 = Label(root, text="Player 2 : 0", font="times 20")
name2.grid(row=1,column=1)

space1 = Label(root, text="      ", font="times 20")
space1.grid(row=0,column=2)

space2 = Label(root, text="      ", font="times 20")
space2.grid(row=1,column=2)

newGame = Label(root, text="New Game", font="times 20")
newGame.grid(row=0,column=3)

resetGame = Label(root, text="Reset game", font="times 20")
resetGame.grid(row=1,column=3)

b1 = Button(root, width = 20, height = 10)
b1.grid(row=2,column=1)

b2 = Button(root, width = 20, height = 10)
b2.grid(row=2,column=2)

b3 = Button(root, width = 20, height = 10)
b3.grid(row=2,column=3)

b4 = Button(root, width = 20, height = 10)
b4.grid(row=3,column=1)

b5 = Button(root, width = 20, height = 10)
b5.grid(row=3,column=2)

b6 = Button(root, width = 20, height = 10)
b6.grid(row=3,column=3)

b7 = Button(root, width = 20, height = 10)
b7.grid(row=4,column=1)

b8 = Button(root, width = 20, height = 10)
b8.grid(row=4,column=2)

b9 = Button(root, width = 20, height = 10)
b9.grid(row=4,column=3)

root.mainloop()