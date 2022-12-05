from tkinter import*
import math

root=Tk()
root.title('Programación pro')
miFrame = Frame(root)
miFrame.pack()

i=0


#--------------------------------Pantalla----------------------------------------------------


pantalla = Entry(miFrame, font="Calibri 15")
pantalla.grid(row=1, column=1, padx=50, pady=50, columnspan=6)
pantalla.config(background='gray', fg='#0a0a0a', justify='left', width=25)



#-------------------------------- pulsaciones teclado --------------------------------------------
def numeroPulsado(num):
    pantalla.insert(END, num)

    
#-------------------------------- función borrar ----------------------------------------------------

def delete():
    pantalla.delete(0,END)
    i=0

#-------------------------------- función borrar un solo elemento ------------------------------------------------

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



# -------------------------------------- functions -----------

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
power = Button(miFrame, text='x^y',width=6, height=1,command=lambda:numeroPulsado('**'), font="Calibri 15").grid(row=2, column=1)

log_e = Button(miFrame, text='ln',width=6, height=1,command=ln, font="Calibri 15").grid(row=3, column=1)

factorial_button = Button(miFrame, text='x!',width=6, height=1,command=fact_func, font="Calibri 15").grid(row=4, column=1)


botonSin = Button(miFrame, text='sin', width=6, height=1, command=trig_sin, font="Calibri 15")
botonSin.grid(row=2,column=2)

botonCos = Button(miFrame, text='cos', width=6, height=1, command=trig_cos, font="Calibri 15")
botonCos.grid(row=2,column=3)

botonTan = Button(miFrame, text='tan', width=6, height=1, command=trig_tan, font="Calibri 15")
botonTan.grid(row=2,column=4)

botonPi = Button(miFrame, text='π', width=6, height=1, command=pi, font="Calibri 15")
botonPi.grid(row=2,column=5)

botonEuler = Button(miFrame, text='e', width=6, height=1, command=e, font="Calibri 15")
botonEuler.grid(row=2,column=6)


#--------------------------------Fila3--------------------------------------------------
boton7 = Button(miFrame, text='7', width=6, height=1, command=lambda:numeroPulsado(7), fg='#354bd8', font="Calibri 15")
boton7.grid(row=3,column=2)

boton8 = Button(miFrame, text='8', width=6, height=1, command=lambda:numeroPulsado(8), fg='#354bd8', font="Calibri 15")
boton8.grid(row=3,column=3)

boton9 = Button(miFrame, text='9', width=6, height=1, command=lambda:numeroPulsado(9), fg='#354bd8', font="Calibri 15")
boton9.grid(row=3,column=4)

botonC = Button(miFrame, text='C', width=6, height=1, font="Calibri 15", command=lambda:delete())
botonC.grid(row=3,column=5)

botonErase = Button(miFrame, text='⌫', width=6, height=1, command=lambda:deleteOne(), font="Calibri 15")
botonErase.grid(row=3,column=6)

#--------------------------------Fila4--------------------------------------------------

boton4 = Button(miFrame, text='4', width=6, height=1, command=lambda:numeroPulsado(4), fg='#354bd8', font="Calibri 15")
boton4.grid(row=4,column=2)

boton5 = Button(miFrame, text='5', width=6, height=1, command=lambda:numeroPulsado(5), fg='#354bd8', font="Calibri 15")
boton5.grid(row=4,column=3)

boton6 = Button(miFrame, text='6', width=6, height=1, command=lambda:numeroPulsado(6), fg='#354bd8', font="Calibri 15")
boton6.grid(row=4,column=4)

boton_multiplica = Button(miFrame, text='*', width=6, height=1, command=lambda:numeroPulsado('*'), font="Calibri 15")
boton_multiplica.grid(row=4,column=5)

boton_div = Button(miFrame, text='÷', width=6, height=1, command=lambda:numeroPulsado('/'), font="Calibri 15")
boton_div.grid(row=4,column=6)

#--------------------------------Fila5--------------------------------------------------

botonOpen = Button(miFrame, text='(', width=6, height=1, command=lambda:numeroPulsado('('), font="Calibri 15")
botonOpen.grid(row=5,column=1)

boton1 = Button(miFrame, text='1', width=6, height=1, command=lambda:numeroPulsado(1), fg='#354bd8', font="Calibri 15")
boton1.grid(row=5,column=2)

boton2 = Button(miFrame, text='2', width=6, height=1, command=lambda:numeroPulsado(2), fg='#354bd8', font="Calibri 15")
boton2.grid(row=5,column=3)

boton3 = Button(miFrame, text='3', width=6, height=1, command=lambda:numeroPulsado(3), fg='#354bd8', font="Calibri 15")
boton3.grid(row=5,column=4)

boton_rest = Button(miFrame, text='-', width=6, height=1, command=lambda:numeroPulsado('-'), font="Calibri 15")
boton_rest.grid(row=5,column=5)

boton_equal = Button(miFrame, text='=', width=6, height=2, command=lambda:operation(), font="Calibri 15")
boton_equal.grid(row=5,column=6, rowspan=2)

#--------------------------------Fila6--------------------------------------------------

botonClose = Button(miFrame, text=')', width=6, height=1, command=lambda:numeroPulsado(')'), font="Calibri 15")
botonClose.grid(row=6,column=1)

boton0 = Button(miFrame, text='0', width=6, height=1, command=lambda:numeroPulsado(0), fg='#354bd8', font="Calibri 15")
boton0.grid(row=6,column=3)

botonPunto = Button(miFrame, text='.', width=6, height=1, command=lambda:numeroPulsado('.'), font="Calibri 15")
botonPunto.grid(row=6,column=4)

boton_sum = Button(miFrame, text='+', width=6, height=1, command=lambda:numeroPulsado('+'), font="Calibri 15")
boton_sum.grid(row=6,column=5)


root.mainloop()