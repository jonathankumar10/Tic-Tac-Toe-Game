from tkinter import *
import tkinter.messagebox


root = Tk()

canvas = Canvas(root)
canvas.pack()

frame = Frame(canvas, relief = RIDGE)
frame.grid(row=1, column = 0)

frameTop = Frame(canvas, relief = RIDGE)
frameTop.grid(row =0, column = 0)

root.title("Tic Tac Toe")

title = Label(frameTop, text="Tic Tac Toe", justify=CENTER, font="times 25", bd = 20, fg='Blue', bg='white')
title.grid(row=0,column=0)

text1 = Entry(frame)
title.grid(row=0,column=2)

text2 = Entry(frame)
title.grid(row=1,column=2)

buttons = StringVar()
click = True

playerX = IntVar()
playerO = IntVar()

playerX.set(0)
playerO.set(0)

def checker(buttons):
    global click
    if buttons["text"] == " " and click == True:
        buttons["text"] = "X"
        click = False
        scorechecker()

    elif buttons["text"] == " " and click == False:
        buttons["text"] = "O"
        click = True
        scorechecker()

def reset():
    b1['text'] = " "
    b2['text'] = " "
    b3['text'] = " "
    b4['text'] = " "
    b5['text'] = " "
    b6['text'] = " "
    b7['text'] = " "
    b8['text'] = " "
    b9['text'] = " "

def newGame():
    reset()
    playerX.set(0)
    playerO.set(0)

def scorechecker():
    if b1["text"]=='X' and b2["text"]=='X' and b3["text"]=='X':
        n = float(playerX.get())
        score = n+1
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X","Player X just won the game. Congradulations!!")
    
    if b4["text"]=='X' and b5["text"]=='X' and b6["text"]=='X':
        n = float(playerX.get())
        score = n+1
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X","Player X just won the game. Congradulations!!")

    if b7["text"]=='X' and b8["text"]=='X' and b9["text"]=='X':
        n = float(playerX.get())
        score = n+1
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X","Player X just won the game. Congradulations!!")

    if b1["text"]=='X' and b5["text"]=='X' and b9["text"]=='X':
        n = float(playerX.get())
        score = n+1
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X","Player X just won the game. Congradulations!!")

    if b3["text"]=='X' and b5["text"]=='X' and b7["text"]=='X':
        n = float(playerX.get())
        score = n+1
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X","Player X just won the game. Congradulations!!")

    if b1["text"]=='X' and b4["text"]=='X' and b7["text"]=='X':
        n = float(playerX.get())
        score = n+1
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X","Player X just won the game. Congradulations!!")

    if b2["text"]=='X' and b5["text"]=='X' and b8["text"]=='X':
        n = float(playerX.get())
        score = n+1
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X","Player X just won the game. Congradulations!!")
    
    if b3["text"]=='X' and b6["text"]=='X' and b9["text"]=='X':
        n = float(playerX.get())
        score = n+1
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X","Player X just won the game. Congradulations!!")
    
    if b1["text"]=='O' and b2["text"]=='O' and b3["text"]=='O':
        n = float(playerO.get())
        score = n+1
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner O","Player O just won the game. Congradulations!!")
    
    if b4["text"]=='O' and b5["text"]=='O' and b6["text"]=='O':
        n = float(playerO.get())
        score = n+1
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner O","Player O just won the game. Congradulations!!")

    if b7["text"]=='O' and b8["text"]=='O' and b9["text"]=='O':
        n = float(playerO.get())
        score = n+1
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner O","Player O just won the game. Congradulations!!")

    if b1["text"]=='O' and b5["text"]=='O' and b9["text"]=='O':
        n = float(playerO.get())
        score = n+1
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner O","Player O just won the game. Congradulations!!")

    if b3["text"]=='O' and b5["text"]=='O' and b7["text"]=='O':
        n = float(playerO.get())
        score = n+1
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner O","Player O just won the game. Congradulations!!")

    if b1["text"]=='O' and b4["text"]=='O' and b7["text"]=='O':
        n = float(playerO.get())
        score = n+1
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner O","Player O just won the game. Congradulations!!")

    if b2["text"]=='O' and b5["text"]=='O' and b8["text"]=='O':
        n = float(playerO.get())
        score = n+1
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner O","Player O just won the game. Congradulations!!")
    
    if b3["text"]=='O' and b6["text"]=='O' and b9["text"]=='O':
        n = float(playerO.get())
        score = n+1
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner O","Player O just won the game. Congradulations!!")

name1 = Label(frame, text="Player 1 : X", font="times 20")
name1.grid(row=1,column=1)

playerXEntry = Entry(frame, textvariable = playerX, width = 14, bd=4, justify = LEFT, font = 30)
playerXEntry.grid(row=1,column=2)

name2 = Label(frame, text="Player 2 : 0", font="times 20")
name2.grid(row=2,column=1)

playerOEntry = Entry(frame, textvariable = playerO, width = 14, bd =4, justify = LEFT,  font = 30)
playerOEntry.grid(row=2,column=2)

newGame = Button(frame, text="New Game", font="times 20", command = newGame)
newGame.grid(row=1,column=3)

resetGame = Button(frame, text="Reset game", font="times 20", command = reset)
resetGame.grid(row=2,column=3)


b1 = Button(frame, width = 20, text=" " ,height = 10, command = lambda: checker(b1))
b1.grid(row=3,column=1)

b2 = Button(frame, width = 20, text=" " , height = 10, command = lambda: checker(b2))
b2.grid(row=3,column=2)

b3 = Button(frame, width = 20, text=" " , height = 10, command = lambda: checker(b3))
b3.grid(row=3,column=3)

b4 = Button(frame, width = 20, text=" " , height = 10, command = lambda: checker(b4))
b4.grid(row=4,column=1)

b5 = Button(frame, width = 20, text=" " , height = 10, command = lambda: checker(b5))
b5.grid(row=4,column=2)

b6 = Button(frame, width = 20, text=" " , height = 10, command = lambda: checker(b6))
b6.grid(row=4,column=3)

b7 = Button(frame, width = 20, text=" " , height = 10, command = lambda: checker(b7))
b7.grid(row=5,column=1)

b8 = Button(frame, width = 20, text=" " , height = 10, command = lambda: checker(b8))
b8.grid(row=5,column=2)

b9 = Button(frame, width = 20, text=" " , height = 10, command = lambda: checker(b9))
b9.grid(row=5,column=3)

root.mainloop()