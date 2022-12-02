def main():
    usuarios=listarUsuarios()
    for usuario in usuarios:
        print (usuario)

def listarUsuarios():
    usuarios=[]
    f=open("/etc/passwd", 'r')
    datos = f.readlines()
    f.close()
    for line in datos:
        if line[0]=='#':
            continue
        if line[0]=='_':
            continue
        partes = line.split(':')
        usuarios.append(partes[0])
    return usuarios

if __name__ =='__main__':
    main()
