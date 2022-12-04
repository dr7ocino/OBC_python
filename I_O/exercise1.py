
class Archivos:
    path =''
    LECTURA='r'
    
    def __init__(self,path,file_name):
        self.path=path
        self.ESCRITURA='r'
        self.LECTURA='a'
        self.file_name=file_name
    def createFile(self):
        try:
            with open(self.file_name, self.LECTURA) as f:
                f.write('Create a new text file')
        except FileNotFoundError:
            print("The directory doesn't exist") 

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