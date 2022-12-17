import tkinter
from tkinter import IntVar, ttk

def seleccion():
    seleccion=f'selecciono la opcion {str(var.get())}'
    label.config(text=seleccion)
def reset():
    var.set(None)
    label.config(text=' ')
window=tkinter.Tk()
var=IntVar()

window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=3)
### opciones
opcion1= ttk.Radiobutton(window, text='opcion 1',variable=var, value=1, command=seleccion)
opcion2= ttk.Radiobutton(window, text='opcion 2',variable=var, value=2, command=seleccion)
opcion3= ttk.Radiobutton(window, text='opcion 3',variable=var, value=3, command=seleccion)
opcion4= ttk.Radiobutton(window, text='opcion 4',variable=var, value=4, command=seleccion)

opcion1.grid(column=0,row=1,sticky=tkinter.E,padx=10,pady=5)
opcion2.grid(column=0,row=2,sticky=tkinter.E,padx=10,pady=5)
opcion3.grid(column=0,row=3,sticky=tkinter.E,padx=10,pady=5)
opcion4.grid(column=0,row=4,sticky=tkinter.E,padx=10,pady=5)
label=ttk.Label(window)
label.grid(column=1,row=5,sticky=tkinter.W,padx=5,pady=5)

### boton de reinicio
button=ttk.Button(text='reset',command=reset)
button.grid(column=0,row=6)
window.mainloop()