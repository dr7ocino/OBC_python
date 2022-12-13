from pickle import *
class Vehiculo:
    def __init__(self, color, puertas):
        self.color=color
        self.puertas=puertas

    def __str__(self) -> str:
        return f'Color: {self.color}, No. puertas: {self.puertas}'

obj=Vehiculo('Rojo', '4')
print(obj)

with open('objeto_vehiculo', 'w+b') as file:
    dump(obj, file)
    file.seek(0)

    nuevo_obj=load(file)
print(nuevo_obj)
