
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
        return data 
        
    def escritura():
    
        pass 


def main():
    path = "/etc/passwd"
    name_file='test.txt'
    data=Archivos(path=path,file_name=name_file)
    datos=data.lectura()
    for read in datos:
        print (read)

if __name__ == '__main__':
    main()
