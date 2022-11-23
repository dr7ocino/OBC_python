#!/bin/python
#programa que verifica si es anio bisiesto.

def bisiesto(year):
    if year%4 == 0:
        return 'es bisiesto'
    else:
        return 'no es bisiesto'

date=input('ingrese anio: ')
print('El anio '+date+' '+bisiesto(int(date)))
