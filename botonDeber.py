def fun1():
    print('David Casa')

def fun2():
    print('nombre2')

def fun3():
    print('nombre3')

def fun4():
    print('nombre4')

from tkinter import *
ventana = Tk()
ventana.title('Deber Botones')
boton1=Button(ventana,text="David Casa",command=fun1)
boton1.grid(row=1,column=1)
boton2=Button(ventana,text="Nombre2",command=fun2)
boton2.grid(row=1,column=2)
boton3=Button(ventana,text="Nombre3",command=fun3)
boton3.grid(row=2,column=1)
boton4=Button(ventana,text="Nombre4",command=fun4)
boton4.grid(row=2,column=2)
