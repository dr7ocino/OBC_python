import sqlite3

def idValue()->int:
    connect=sqlite3.connect('Alumnos.db')
    cursor=connect.cursor()
    query=f"SELECT * FROM alumnos ORDER BY id DESC LIMIT 1"
    row=cursor.execute(query)
    data=row.fetchone()
    cursor.close()
    connect.close()
    print(data[0])
    if data==None:
        return 0
    return int(data[0])

def crearAlumno( name, last_name):
    identificador=int(idValue())+1
    connect=sqlite3.connect('Alumnos.db')
    cursor=connect.cursor()
    query=f'''INSERT INTO alumnos(id, name, last_name) VALUES(?,?,?)'''
    rows = cursor.execute(query, (identificador, name, last_name))
    connect.commit()
    cursor.close()
    connect.close()

def validacionAlumno(nombre):
    connect=sqlite3.connect('Alumnos.db')
    cursor=connect.cursor()
    query=f'''SELECT * FROM alumnos WHERE name='{nombre}' '''
    rows=cursor.execute(query)
    data=rows.fetchone()
    cursor.close()
    connect.close()
    if data==None:
        return f'NO Existe El usuario {nombre}'
    return data

user=['juan','marcos','diego','alvin']
apellidos=['ruga','chuquimia','relv','coma']
for i in range(0,len(user)):
    crearAlumno(name=user[i], last_name=apellidos[i])
print(validacionAlumno("Carlos")) 
print(validacionAlumno("fulanito"))   