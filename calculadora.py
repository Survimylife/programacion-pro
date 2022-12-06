from tkinter import*

import math

root=Tk() # create root window
root.title('Programación pro') # title of the GUI window
root.maxsize(344,417) #(witdh, height) specify the max size the window can expand to
root.config(bg="skyblue")  # specify background color
root.iconbitmap('C:\programacion-pro\calcu4.ico')
miFrame = Frame(root)
miFrame.config(cursor="mouse",bg="#ffffff",relief="sunken")
miFrame.pack()



i=0

"""root=Tk() # create root window
root.title('Programación pro') # title of the GUI window
root.maxsize(500,400) # specify the max size the window can expand to
image = tk.PhotoImage(file="cat.gif")
original_image = image.subsample(1,1)  # resize image using subsample
root.config(bg="skyblue")  # specify background color
miFrame = Label(root,i=original_image)
miFrame.config(cursor="mouse",bg="skyblue",relief="sunken",bd=10)
miFrame.pack()"""

#--------------------------------Pantalla----------------------------------------------------


pantalla = Entry(miFrame, font="Calibri 20")
pantalla.grid(row=1, column=1, padx=30, pady=70, columnspan=6)
pantalla.config(background='#b1b3dc', fg='#0a0a0a', justify='left', width=20)



#-------------------------------- pulsaciones teclado --------------------------------------------
def numeroPulsado(num):
    pantalla.insert(END, num)

    
#-------------------------------- función borrar ----------------------------------------------------

def delete():
    pantalla.delete(0,END)
    i=0

#-------------------------------- función borrar un solo elemento ---------------------------------

def deleteOne():
    pantalla_status = pantalla.get()
    if len(pantalla_status):
        pantalla_new_status = pantalla_status[:-1]
        delete()
        pantalla.insert(0, pantalla_new_status)
    else:
        delete()

#-------------------------------- función operaciones ------------------------------------------------

def operation():
    try:
        result = eval(pantalla.get().replace('^','**'))
    except: 
        delete()
        result = "ERROR"
    pantalla.delete(0,END)
    pantalla.insert(0, result)



# -------------------------------------- functions -------------------------------------------

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

def fact_func():
    number = pantalla.get()
    result = str(factorial(int(number)))
    pantalla.delete(0,END)
    pantalla.insert(0,result)

# sine

def trig_sin():
    number = pantalla.get()
    result = str(math.sin(math.radians(float(number))))
    pantalla.delete(0,END)
    pantalla.insert(0,result)

# cosine

def trig_cos():
    number = pantalla.get()
    result = str(math.cos(math.radians(float(number))))
    pantalla.delete(0,END)
    pantalla.insert(0,result)

# tan

def trig_tan():
    number = pantalla.get()
    result = str(math.tan(math.radians(float(number))))
    pantalla.delete(0,END)
    pantalla.insert(0,result)

def ln():
    number = pantalla.get()
    result = str(math.log(float(number)))
    pantalla.delete(0,END)
    pantalla.insert(0,result)

def e():
    result = str(math.exp(1))
    pantalla.delete(0,END)
    pantalla.insert(0,result)

def pi():
    pantalla.delete(0,END)
    pantalla.insert(0,math.pi)



#--------------------------------Fila2--------------------------------------------------
power = Button(miFrame, text='x^y', width=4, height=1, command=lambda:numeroPulsado('**'),
 font="Calibri 15", relief='groove').grid(row=2, column=1, padx=3, pady=3)

log_e = Button(miFrame, text='ln', width=4, height=1,command=ln,
 font="Calibri 15", relief='groove').grid(row=3, column=1)

factorial_button = Button(miFrame, text='x!', width=4, height=1,command=fact_func,
 font="Calibri 15", relief='groove').grid(row=4, column=1, padx=3, pady=3)

botonSin = Button(miFrame, text='sin', width=4, height=1, command=trig_sin, font="Calibri 15",
 relief='groove')
botonSin.grid(row=2, column=2, padx=3, pady=3)

botonCos = Button(miFrame, text='cos', width=4, height=1, command=trig_cos, font="Calibri 15",
 relief='groove')
botonCos.grid(row=2, column=3, padx=3, pady=3)

botonTan = Button(miFrame, text='tan', width=4, height=1, command=trig_tan, font="Calibri 15",
 relief='groove')
botonTan.grid(row=2, column=4, padx=3, pady=3)

botonPi = Button(miFrame, text='π', width=4, height=1, command=pi, font="Calibri 15",
 relief='groove')
botonPi.grid(row=2, column=5, padx=3, pady=3)

botonEuler = Button(miFrame, text='e', width=4, height=1, command=e, font="Calibri 15",
 relief='groove')
botonEuler.grid(row=2, column=6, padx=3, pady=3)


#--------------------------------Fila3--------------------------------------------------
boton7 = Button(miFrame, text='7', width=4, height=1, command=lambda:numeroPulsado(7), fg='#354bd8',
 font="Calibri 15", background='#ebebee', relief='flat')
boton7.grid(row=3, column=2, padx=3, pady=3)

boton8 = Button(miFrame, text='8', width=4, height=1, command=lambda:numeroPulsado(8), fg='#354bd8',
 font="Calibri 15", background='#ebebee', relief='flat')
boton8.grid(row=3, column=3, padx=3, pady=3)

boton9 = Button(miFrame, text='9', width=4, height=1, command=lambda:numeroPulsado(9), fg='#354bd8',
 font="Calibri 15", background='#ebebee', relief='flat')
boton9.grid(row=3, column=4, padx=3, pady=3)

botonC = Button(miFrame, text='C', width=4, height=1, font="Calibri 15", fg='#0022ff',
 command=lambda:delete(), relief='flat', underline=5)
botonC.grid(row=3, column=5, padx=3, pady=3)

botonErase = Button(miFrame, text='⌫', width=4, height=1, command=lambda:deleteOne(), fg='#0022ff',
 font="Calibri 15", relief='flat', underline=5)
botonErase.grid(row=3, column=6, padx=3, pady=3)

#--------------------------------Fila4--------------------------------------------------

boton4 = Button(miFrame, text='4', width=4, height=1, command=lambda:numeroPulsado(4), fg='#354bd8',
 font="Calibri 15", background='#ebebee', relief='flat')
boton4.grid(row=4, column=2, padx=3, pady=3)

boton5 = Button(miFrame, text='5', width=4, height=1, command=lambda:numeroPulsado(5), fg='#354bd8',
 font="Calibri 15", background='#ebebee', relief='flat')
boton5.grid(row=4, column=3, padx=3, pady=3)

boton6 = Button(miFrame, text='6', width=4, height=1, command=lambda:numeroPulsado(6), fg='#354bd8',
 font="Calibri 15", background='#ebebee', relief='flat')
boton6.grid(row=4, column=4, padx=3, pady=3)

boton_multiplica = Button(miFrame, text='*', width=4, height=1, command=lambda:numeroPulsado('*'),
 font="Calibri 15", background='#b1b3dc', relief='flat')
boton_multiplica.grid(row=4, column=5, padx=3, pady=3)

boton_div = Button(miFrame, text='÷', width=4, height=1, command=lambda:numeroPulsado('/'),
 font="Calibri 15", background='#b1b3dc', relief='flat')
boton_div.grid(row=4, column=6, padx=3, pady=3)

#--------------------------------Fila5--------------------------------------------------

botonOpen = Button(miFrame, text='(', width=4, height=1, command=lambda:numeroPulsado('('),
 font="Calibri 15", relief='groove')
botonOpen.grid(row=5, column=1, padx=3, pady=3)

boton1 = Button(miFrame, text='1', width=4, height=1, command=lambda:numeroPulsado(1), fg='#354bd8',
 font="Calibri 15", background='#ebebee', relief='flat')
boton1.grid(row=5, column=2, padx=3, pady=3)

boton2 = Button(miFrame, text='2', width=4, height=1, command=lambda:numeroPulsado(2), fg='#354bd8',
 font="Calibri 15", background='#ebebee', relief='flat')
boton2.grid(row=5, column=3, padx=3, pady=3)

boton3 = Button(miFrame, text='3', width=4, height=1, command=lambda:numeroPulsado(3), fg='#354bd8',
 font="Calibri 15", background='#ebebee', relief='flat')
boton3.grid(row=5, column=4, padx=3, pady=3)

boton_rest = Button(miFrame, text='-', width=4, height=1, command=lambda:numeroPulsado('-'),
 font="Calibri 15", background='#b1b3dc', relief='flat')
boton_rest.grid(row=5, column=5, padx=3, pady=3)

boton_equal = Button(miFrame, text='=', width=4, height=3, command=lambda:operation(),
 font="Calibri 15", background='#b1b3dc', relief='flat')
boton_equal.grid(row=5, column=6, rowspan=2, padx=3, pady=3)

#--------------------------------Fila6--------------------------------------------------

botonClose = Button(miFrame, text=')', width=4, height=1, command=lambda:numeroPulsado(')'),
 font="Calibri 15", relief='groove')
botonClose.grid(row=6, column=1, padx=3, pady=3)

boton0 = Button(miFrame, text='0', width=4, height=1, command=lambda:numeroPulsado(0), fg='#354bd8',
 font="Calibri 15", background='#ebebee', relief='flat')
boton0.grid(row=6, column=3, padx=3, pady=3)

botonPunto = Button(miFrame, text='.', width=4, height=1, command=lambda:numeroPulsado('.'),
 font="Calibri 15", background='#ebebee', relief='flat')
botonPunto.grid(row=6, column=4, padx=3, pady=3)

boton_sum = Button(miFrame, text='+', width=4, height=1, command=lambda:numeroPulsado('+'),
 font="Calibri 15", background='#b1b3dc', relief='flat')
boton_sum.grid(row=6, column=5, padx=3, pady=3)


root.mainloop()