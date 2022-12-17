import tkinter
def saludar(event):
    print('se ha hecho click en saludar')
def saludarDobleClick(event):
    print('Se ha hecho un doble Click')
def salir(event):
    print('Exit:')
    window.quit()
window = tkinter.Tk()
boton=tkinter.Button(window, text='haz click')
boton.pack()
boton.bind('<Button-1>',saludar)
boton.bind('<Double-1>',saludarDobleClick)
## exit
botonExit=tkinter.Button(window, text='Exit')
botonExit.pack()
botonExit.bind('<Button-1>',salir)


window.mainloop()