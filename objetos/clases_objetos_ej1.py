#! /usr/bin/python
'''
En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
* Color
* Ruedas
* Puertas

Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
* Velocidad
* Cilindrada
Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.
'''

class Vehiculo :
    color = 'Rojo'
    ruedas = 4
    puertas = 4

class Coche(Vehiculo):
    Velocidad = '60 km/h'
    cilindrada = '250cc'
    
obj = Coche()
