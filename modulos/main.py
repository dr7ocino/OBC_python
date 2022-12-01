import modules.operaciones as mo 
def main():
    operaciones = mo.Operaciones(8,4)
    suma=operaciones.suma()
    resta=operaciones.resta()
    multi=operaciones.multiplicacion()
    div=operaciones.division()
    print(suma)
if __name__ == '__main__':
    main()
