from tkinter import*

root=Tk()
root.title('Programación pro')
miFrame = Frame(root)
miFrame.pack()

i=0
#--------------------------------Pantalla----------------------------------------------------


pantalla = Entry(miFrame, font="Calibri 10")
pantalla.grid(row=1, column=1, padx=50, pady=50, columnspan=6)
pantalla.config(background='gray', fg='#0a0a0a', justify='left', width=40)

#-------------------------------- pulsaciones teclado --------------------------------------------
def numeroPulsado(num):
    global i
    pantalla.insert(i, num)
    i += 1
    
#-------------------------------- función borrar ----------------------------------------------------

def delete():
    pantalla.delete(0,END)
    i=0

#-------------------------------- función borrar un solo elemento ------------------------------------------------
""""
def deleteOne():
    pantalla = pantalla.get()
    if len(pantalla):
        pantalla_nuevo = pantalla[:-1]
        clear_pantalla()
        pantalla.insert(pantalla_nuevo)
    i=0
"""
#-------------------------------- función operaciones ------------------------------------------------

def operation():
    ecuacion = pantalla.get()
    result = eval(ecuacion)
    pantalla.delete(0,END)
    pantalla.insert(0, result)
    i=0

#--------------------------------Fila2--------------------------------------------------

botonSin = Button(miFrame, text='sin', width=6, height=2, command=lambda:numeroPulsado('sin'))
botonSin.grid(row=2,column=2)

botonCos = Button(miFrame, text='cos', width=6, height=2, command=lambda:numeroPulsado('cos'))
botonCos.grid(row=2,column=3)

botonTan = Button(miFrame, text='tan', width=6, height=2, command=lambda:numeroPulsado('tan'))
botonTan.grid(row=2,column=4)

botonPi = Button(miFrame, text='π', width=6, height=2, command=lambda:numeroPulsado('π'))
botonPi.grid(row=2,column=5)

botonEuler = Button(miFrame, text='e', width=6, height=2, command=lambda:numeroPulsado('e'))
botonEuler.grid(row=2,column=6)


#--------------------------------Fila3--------------------------------------------------
boton7 = Button(miFrame, text='7', width=6, height=2, command=lambda:numeroPulsado(7), fg='#354bd8')
boton7.grid(row=3,column=2)

boton8 = Button(miFrame, text='8', width=6, height=2, command=lambda:numeroPulsado(8), fg='#354bd8')
boton8.grid(row=3,column=3)

boton9 = Button(miFrame, text='9', width=6, height=2, command=lambda:numeroPulsado(9), fg='#354bd8')
boton9.grid(row=3,column=4)

botonC = Button(miFrame, text='C', width=6, height=2, font=("Times", 10), command=lambda:delete())
botonC.grid(row=3,column=5)

botonErase = Button(miFrame, text='⌫', width=6, height=2, command=lambda:deleteOne())
botonErase.grid(row=3,column=6)

#--------------------------------Fila4--------------------------------------------------

boton4 = Button(miFrame, text='4', width=6, height=2, command=lambda:numeroPulsado(4), fg='#354bd8')
boton4.grid(row=4,column=2)

boton5 = Button(miFrame, text='5', width=6, height=2, command=lambda:numeroPulsado(5), fg='#354bd8')
boton5.grid(row=4,column=3)

boton6 = Button(miFrame, text='6', width=6, height=2, command=lambda:numeroPulsado(6), fg='#354bd8')
boton6.grid(row=4,column=4)

boton_multiplica = Button(miFrame, text='*', width=6, height=2, command=lambda:numeroPulsado('*'))
boton_multiplica.grid(row=4,column=5)

boton_div = Button(miFrame, text='÷', width=6, height=2, command=lambda:numeroPulsado('/'))
boton_div.grid(row=4,column=6)

#--------------------------------Fila5--------------------------------------------------

botonOpen = Button(miFrame, text='(', width=6, height=2, command=lambda:numeroPulsado('('))
botonOpen.grid(row=5,column=1)

boton1 = Button(miFrame, text='1', width=6, height=2, command=lambda:numeroPulsado(1), fg='#354bd8')
boton1.grid(row=5,column=2)

boton2 = Button(miFrame, text='2', width=6, height=2, command=lambda:numeroPulsado(2), fg='#354bd8')
boton2.grid(row=5,column=3)

boton3 = Button(miFrame, text='3', width=6, height=2, command=lambda:numeroPulsado(3), fg='#354bd8')
boton3.grid(row=5,column=4)

boton_rest = Button(miFrame, text='-', width=6, height=2, command=lambda:numeroPulsado('-'))
boton_rest.grid(row=5,column=5)

boton_equal = Button(miFrame, text='=', width=6, height=4, command=lambda:operation())
boton_equal.grid(row=5,column=6, rowspan=2)

#--------------------------------Fila6--------------------------------------------------

botonClose = Button(miFrame, text=')', width=6, height=2, command=lambda:numeroPulsado(')'))
botonClose.grid(row=6,column=1)

boton0 = Button(miFrame, text='0', width=6, height=2, command=lambda:numeroPulsado(0), fg='#354bd8')
boton0.grid(row=6,column=3)

botonPunto = Button(miFrame, text='.', width=6, height=2, command=lambda:numeroPulsado('.'))
botonPunto.grid(row=6,column=4)

boton_sum = Button(miFrame, text='+', width=6, height=2, command=lambda:numeroPulsado('+'))
boton_sum.grid(row=6,column=5)


"""numeroPantalla = StringVar()

pantalla = Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=50, pady=50, columnspan=6)
pantalla.config(background='gray', fg='#0a0a0a', justify='right', width=40)

#--------------------------------pulsaciones teclado----------------------------------------------------
def numeroPulsado(num):
    numeroPantalla.set(numeroPantalla.get() + num)"""

root.mainloop()