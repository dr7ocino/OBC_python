import getpass
import sqlite3
def verificacionCredenciales(username, password):
    connect=sqlite3.connect('miaplicacion3.db',isolation_level=None)#usamos isulation_Level para no tener que colocar commit cada vez que modificamos algo
    cursor= connect.cursor()
    query=f"SELECT id FROM users WHERE username='{username}' AND password='{password}'"
    valor=cursor.execute(query)
    data=valor.fetchone()
    cursor.close()
    connect.close()
    if data =='None':
        return False
    return True

def crearUsuario():
    #INSERT TO users(id, username, password) VALUES(?,?,?)
    ## agregamos los valores con el metod execute mediante tupla    
    pass

def main():
    username=input('Nombre de usuario: ')
    password= getpass.getpass('contrasena: ')
    if verificacionCredenciales(username=username, password=password):
        print('login correcto')
    else: 
        print('login incorrecto')


if __name__=='__main__':
    main()


