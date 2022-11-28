#!/bin/python
#programa que verifica si es anio bisiesto.

def bisiesto(year):
    if year%4 == 0:
        return 'es bisiesto'
    else:
        return 'no es bisiesto'

date=input('ingrese anio: ')
print('El anio '+date+' '+bisiesto(int(date)))


class Dino:
    _encendido=True
    def enciende(self):
        print('se ha encendido')
        self._encendido=True
    def apaga(self):
        print('se ha apagado')
        self._encendido=False
    def isEncendido(self):
        return self._encendido

d1 = Dino()
d1.apaga()
print(d1.isEncendido)