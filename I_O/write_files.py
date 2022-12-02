import pickle #serializamos datos en archivos .bin

"""
la serializacion es muy util para guardar estados de un objeto
sin necesidad de usar bases de datos
"""
lista=['item','linea2','item3']


def escribe(fichero, datos):
    f=open(fichero,'a')#usamos la letra por append
    for linea in datos:
        if linea.endswith('\n')==False:# otra forma if not linea.endswith('\r')
            linea = linea +'\n'
        f.write(linea)
        #f.writelines(lista)
#f.write('datos\n')
#f.write('datos2')
    f.close

class Juguete:
    nombre=''
    precio=0.0
    def __init__(self, nombre, precio):
        self.nombre=nombre
        self.precio=precio
    def getNombre(self):
        return self.nombre

j1=Juguete('Papa', 10.5)
print(type(j1))
print(j1.getNombre())

f = open('datos.txt','wb')
pickle.dump(j1, f)
f.close()
        


escribe('mifichero.txt',lista)
