
class Archivos:
    path =''
    LECTURA='r'
    
    def __init__(self,path):
        self.path=path
        self.ESCRITURA='a'
        self.LECTURA='r'
    
    def lectura(self):
        f=open(self.path, self.LECTURA)
        data=f.readlines()
        f.close()
        return data 
        
    def escritura():
    
        pass 


def main():
    path = "/etc/passwd"
    data=Archivos(path)
    datos=data.lectura()
    for read in datos:
        print (read)

if __name__ == '__main__':
    main()
