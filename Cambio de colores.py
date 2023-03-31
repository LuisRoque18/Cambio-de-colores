from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import colorchooser as ColorChooser
root= Tk()

def cambiarcolor():
    print("#"+rojo.get()+verde.get()+azul.get())
    cambio = rojo.get()+verde.get()+azul.get()

    if len(cambio)>6:
        alerta.config(text=f'Se introdujeron más\n de 6 digitos')

    elif len(cambio)<6:
        alerta.config(text=f'Se introdujeron menos\n de 6 digitos')

    else:
        ventana.config(bg=("#"+rojo.get()+verde.get()+azul.get()))

rojo = StringVar()
verde = StringVar()
azul = StringVar()
ventana = Frame(root)
ventana.pack(fill='both', expand=1)
root.geometry("200x150")

etiquetarojo = Label(ventana, text="RED")
etiquetarojo.grid(row=1, column=2, padx=2, pady=2)
entradarojo = Entry(ventana, textvariable=rojo)
entradarojo.grid(row=1, column=3)

etiquetaverde = Label(ventana, text="GREEN")
etiquetaverde.grid(row=2, column=2, padx=2, pady=2)
entradaverde = Entry(ventana, textvariable=verde)
entradaverde.grid(row=2, column=3)

etiquetaAzul = Label(ventana, text="BLUE")
etiquetaAzul.grid(row=3, column=2, padx=2, pady=2)
entradaAzul = Entry(ventana, textvariable=azul)
entradaAzul.grid(row=3, column=3)

boton = Button(ventana, text="Cambiar color",command=cambiarcolor)
boton.grid(row=5, column=3)

alerta = Label(ventana, text="")
alerta.grid(row=7,column=3)

root.mainloop()