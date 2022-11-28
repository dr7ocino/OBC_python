#!/usr/bin/python
class Alumnos:
    def __init__(self, nombre, nota ) :
        self.nombre = nombre 
        self.nota = nota
        self.stat=''
    def status(self):
        if (self.nota >=6):
            self.stat='Aprobado'
        else:
            self.stat='reprobado'
        return self.stat
    def __str__(self):
        return 'Estudiante: {}, Nota: {}, Estado: {}'.format(self.nombre, self.nota, self.stat)

alumno=Alumnos('carlos',7)
alumno.status()
print(alumno)