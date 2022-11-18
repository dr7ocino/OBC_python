#Escribe un programa que sea capaz de mostrar los números del 1 al 100 en orden inverso.
Lista_generada=[]
for lista in range(1,101):
    Lista_generada.append(lista)
lista_ordenada=sorted(Lista_generada, reverse=True)
for number in lista_ordenada:
    print (number)
    