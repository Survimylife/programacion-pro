from tkinter import* 

import math

root = Tk() # create root window
root.title('Programación pro') # title of the GUI window
root.maxsize(336,381) # (witdh, height) specify the max size the window can expand to
root.config(bg="skyblue")  # specify background color
# root.iconbitmap('C:\programacion-pro\calcu4.ico')
miFrame = Frame(root)
miFrame.config(cursor="mouse", bg="#ffffff", relief="sunken") # background
miFrame.pack() # position

#----------------------------------------------- Pantalla -----------------------------------------------

pantalla = Entry(miFrame, font="Calibri 30")
pantalla.grid(row=0, column=1, padx=10, pady=20, columnspan=6)
pantalla.config(background='#b1b3dc', fg='#0a0a0a', justify='left', width=15)

#------------------------------------------ Pulsaciones teclado ------------------------------------------

def numeroPulsado(num):
    pantalla.insert(END, num)

#-------------------------------------------- Función borrar --------------------------------------------

i=0

def delete():
    pantalla.delete(0,END)
    i=0

#------------------------------------ Función borrar un solo elemento ------------------------------------

def deleteOne():
    pantalla_status = pantalla.get()
    if len(pantalla_status):
        pantalla_new_status = pantalla_status[:-1]
        delete()
        pantalla.insert(0, pantalla_new_status)
    else:
        delete()

#---------------------------- Logaritmo natural, radicación y Trignométricas ----------------------------

def operation():
    try:
        gt=pantalla.get()
        if 'sin' in gt:
            gt=pantalla.get().replace('sin','')
            result = str(math.sin(math.radians(float(gt))))
        elif 'cos' in gt:
            gt=pantalla.get().replace('cos','')
            result = str(math.cos(math.radians(float(gt))))
        elif 'tan' in gt:
            gt=pantalla.get().replace('tan','')
            result = str(math.tan(math.radians(float(gt))))
        elif 'arcsn' in gt:
            gt=pantalla.get().replace('arcsn','')
            result = str(math.asin(math.radians(float(gt))))
        elif 'arccs' in gt:
            gt=pantalla.get().replace('arccs','')
            result = str(math.acos(math.radians(float(gt))))
        elif 'arctn' in gt:
            gt=pantalla.get().replace('arctn','')
            result = str(math.atan(math.radians(float(gt))))
        elif 'ln' in gt:
            gt=pantalla.get().replace('ln','')
            result = str(math.log(float(gt)))
        elif '√' in gt:
            gt=pantalla.get().replace('√','')
            result = str(math.sqrt(float(gt)))
        else:
            result = eval(pantalla.get().replace('^','**'))
    except: 
        delete()
        result = "ERROR"
    pantalla.delete(0,END)
    pantalla.insert(0, result)

#----------------------------------------- Euler, factorial y pi -----------------------------------------

def e():
    result = str(math.exp(1))
    pantalla.insert(END,result)

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

def pi():
    pantalla.insert(END,math.pi)

#------------------------------------------------ Fila 1 ------------------------------------------------

boton_modulo = Button(miFrame, text='mod', width=4, height=1, command=lambda:numeroPulsado('%'),
 font="Calibri 15", relief='groove')
boton_modulo.grid(row=1,column=1)

botonSinInv = Button(miFrame, text='sin-1', width=4, height=1, command=lambda:numeroPulsado('arcsn'),
 background='#d6f3d4', font="Calibri 15", relief='groove')
botonSinInv.grid(row=1, column=2, padx=3, pady=3)

botonCosInv = Button(miFrame, text='cos-1', width=4, height=1, command=lambda:numeroPulsado('arccs'),
 background='#d6f3d4', font="Calibri 15", relief='groove')
botonCosInv.grid(row=1, column=3, padx=3, pady=3)

botonTanInv = Button(miFrame, text='tan-1', width=4, height=1, command=lambda:numeroPulsado('arctn'),
 background='#d6f3d4', font="Calibri 15", relief='groove')
botonTanInv.grid(row=1, column=4, padx=3, pady=3)

botonfi = Button(miFrame, text='NA', width=4, height=1, command=lambda:numeroPulsado('6.02214076*10^23'),
 font="Calibri 15", relief='groove')
botonfi.grid(row=1, column=5, padx=3, pady=3)

botong = Button(miFrame, text='g', width=4, height=1, command=lambda:numeroPulsado('9.80665'),
 font="Calibri 15", relief='groove')
botong.grid(row=1, column=6, padx=3, pady=3)

#------------------------------------------------ Fila 2 ------------------------------------------------

power = Button(miFrame, text='x^y', width=4, height=1, command=lambda:numeroPulsado('^'),
 font="Calibri 15", relief='groove').grid(row=2, column=1, padx=3, pady=3)

botonSin = Button(miFrame, text='sin', width=4, height=1, command=lambda:numeroPulsado('sin'),
 background='#d6f3d4', font="Calibri 15", relief='groove')
botonSin.grid(row=2, column=2, padx=3, pady=3)

botonCos = Button(miFrame, text='cos', width=4, height=1, command=lambda:numeroPulsado('cos'),
 background='#d6f3d4', font="Calibri 15", relief='groove')
botonCos.grid(row=2, column=3, padx=3, pady=3)

botonTan = Button(miFrame, text='tan', width=4, height=1, command=lambda:numeroPulsado('tan'),
 background='#d6f3d4', font="Calibri 15", relief='groove')
botonTan.grid(row=2, column=4, padx=3, pady=3)

botonPi = Button(miFrame, text='π', width=4, height=1, command=pi, font="Calibri 15",
 relief='groove')
botonPi.grid(row=2, column=5, padx=3, pady=3)

botonEuler = Button(miFrame, text='e', width=4, height=1, command=e, font="Calibri 15",
 relief='groove')
botonEuler.grid(row=2, column=6, padx=3, pady=3)

#------------------------------------------------ Fila 3 ------------------------------------------------

log_e = Button(miFrame, text='ln', width=4, height=1,command=lambda:numeroPulsado('ln'),
 font="Calibri 15", relief='groove').grid(row=3, column=1, padx=3, pady=3)

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

#----------------------------------------------- Fila 4 -----------------------------------------------

factorial_button = Button(miFrame, text='x!', width=4, height=1,command=fact_func,
 font="Calibri 15", relief='groove').grid(row=4, column=1, padx=3, pady=3)

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

#------------------------------------------------ Fila5 -------------------------------------------------

boton_raiz = Button(miFrame, text='√', width=4, height=1, command=lambda:numeroPulsado('√'),
 font="Calibri 15", relief='groove')
boton_raiz.grid(row=5,column=1)

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

#------------------------------------------------- Fila6 ------------------------------------------------

botonOpen = Button(miFrame, text='(', width=4, height=1, command=lambda:numeroPulsado('('),
 font="Calibri 15", relief='groove')
botonOpen.grid(row=6, column=1, padx=3, pady=3)

botonClose = Button(miFrame, text=')', width=4, height=1, command=lambda:numeroPulsado(')'),
 font="Calibri 15", relief='groove')
botonClose.grid(row=6, column=2, padx=3, pady=3)

boton0 = Button(miFrame, text='0', width=4, height=1, command=lambda:numeroPulsado(0), fg='#354bd8',
 font="Calibri 15", background='#ebebee', relief='flat')
boton0.grid(row=6, column=3, padx=3, pady=3)

botonPunto = Button(miFrame, text='.', width=4, height=1, command=lambda:numeroPulsado('.'),
 font="Calibri 15", background='#ebebee', relief='flat')
botonPunto.grid(row=6, column=4, padx=3, pady=3)

boton_sum = Button(miFrame, text='+', width=4, height=1, command=lambda:numeroPulsado('+'),
 font="Calibri 15", background='#b1b3dc', relief='flat')
boton_sum.grid(row=6, column=5, padx=3, pady=3)


root.mainloop()  # last logical line of code in your program