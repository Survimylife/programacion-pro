from tkinter import*

root = Tk()

root.title('Calculadora')

#root.iconbitmap()

root.config(bg='black')
miFrame = Frame()
miFrame.pack(side='top')
miFrame.config(bg='red', cursor='hand1', width='400', height='500')
root.mainloop()