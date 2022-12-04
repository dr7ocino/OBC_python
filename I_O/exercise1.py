
class Archivos:
    path =''
    LECTURA='r'
    
    def __init__(self,file_name):
        #self.path=path
        self.ESCRITURA='a'
        self.LECTURA='r'
        self.file_name=file_name
    def createFile(self):
        try:
            with open(self.file_name, 'w') as f:
                f.write('Welcome to my text file\n')
                print(f'Create a new file: {self.file_name}\n')
        except FileNotFoundError:
            print("The directory doesn't exist") 

    def lectura(self):
        f=open(self.file_name, self.LECTURA)
        data=f.readlines()
        f.close()
        return data 
        
    def escritura(self):
         f=open(self.file_name,self.ESCRITURA)
         f.write("I'm writting a line\n")


def main():
    #path = "/etc/passwd"
    name_file='test.txt'
    data=Archivos(file_name=name_file)
    #datos=data.lectura()
    data.createFile()
    data.escritura()
    datos=data.lectura()
    for read in datos:
        print (read)

if __name__ == '__main__':
    main()
