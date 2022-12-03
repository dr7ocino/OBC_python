
class Archivos:
    path =''
    LECTURA='r'
    
    def __init__(self,path):
        self.path=path
        self.ESCRITURA='r'
        self.LECTURA='a'
    
    def lectura(self):
        f=open(self.path, self.LECTURA)
        data=f.readlines()
        f.close()
        return f 
        
    def escritura():
    
        pass 


def main():
    path = r"C:\\Users\\dr7ocino\\Downloads\\map.txt"
    data=Archivos(path)
    data.lectura()
    for read in data:
        print (read)

if __name__ == '__main__':
    main()