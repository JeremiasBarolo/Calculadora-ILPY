#Programa creado por Jeremias Barolo.

#Invocaciones
from tkinter import *

#Root
root = Tk()
root.title("Calculadora")
root.configure(background="#333333")
root.geometry("386x168")
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)
root.grid_rowconfigure(0,weight=1)

#Display
equation= StringVar()

#Funciones
def clear():
    equation.set("")
    
def equalpress():
    try:
        total= str(eval(equation.get()))
        equation.set(total)
    except:
        equation.set("ERROR")

def press(num):
    print(num)
    equation.set(equation.get() + str(num))
    print(equation.get())

#Entry 
expresion_entry = Entry(root, textvariable=equation)
expresion_entry.grid(row=0,column=0, columnspan=4,rowspan=2, sticky="nswe") 

#Botones
btn7 = Button(root, text=" 7 ",foreground="#fff", background="#666", command=lambda: press(7)) 
btn7.grid(row=2 ,column=0, sticky="nswe")

btn8 = Button(root, text=" 8 ",foreground="#fff", background="#666", command=lambda: press(8))
btn8.grid(row=2, column=1, sticky="nswe")

btn9 = Button(root, text=" 9 ",foreground="#fff", background="#666",command=lambda: press(9))
btn9.grid(row=2, column=2, sticky="nswe")

btn4 = Button(root, text=" 4 ",foreground="#fff", background="#666", command=lambda: press(4))
btn4.grid(row=3, column=0, sticky="nswe")

btn5 = Button(root, text=" 5 ",foreground="#fff", background="#666",command=lambda: press(5))
btn5.grid(row=3, column=1, sticky="nswe")

btn6 = Button(root, text=" 6 ",foreground="#fff", background="#666", command=lambda: press(6))
btn6.grid(row=3, column=2, sticky="nswe")

btn3 = Button(root, text=" 3 ",foreground="#fff", background="#666", command=lambda: press(3))
btn3.grid(row=4, column=0, sticky="nswe")

btn2 = Button(root, text=" 2 ",foreground="#fff", background="#666", command=lambda: press(2))
btn2.grid(row=4, column=1, sticky="nswe")

btn1 = Button(root, text=" 1 ",foreground="#fff", background="#666", command=lambda: press(1))
btn1.grid(row=4, column=2, sticky="nswe")

btn0 = Button(root, text=" 0 ",foreground="#fff", background="#666", command=lambda: press(0))
btn0.grid(row=5, column=0, sticky="nswe", columnspan=2)

btndecimal = Button(root, text=" . ",foreground="#fff", background="#666", command=lambda: press("."))
btndecimal.grid(row=5, column=2, sticky="nswe")

plus = Button(root, text=" + ",foreground="#fff", background="#Fe9727", command=lambda: press("+"))
plus.grid(row=2, column=3, sticky="nswe")

minus = Button(root, text=" - ",foreground="#fff", background="#Fe9727", command=lambda: press("-"))
minus.grid(row=3, column=3, sticky="nswe")

multiplication = Button(root, text=" x ",foreground="#fff", background="#Fe9727", command=lambda: press("*"))
multiplication.grid(row=4, column=3, sticky="nswe")

divide = Button(root, text=" % ",foreground="#fff", background="#Fe9727", command=lambda: press("/"))   
divide.grid(row=5, column=3, sticky="nswe")

equal= Button(root, text=" = ",foreground="#fff", background="#Fe9727", command=equalpress)
equal.grid(row=6, column=3, sticky="nswe")

clear= Button(root, text=" Clear ",foreground="#fff", background="#999", command=clear)
clear.grid(row=6, column=0,columnspan= 3 ,sticky="nswe")



root.mainloop()
 