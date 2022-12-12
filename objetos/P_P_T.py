import random 

class Game:
    def __init__(self,):
        self.estados={1:'Piedra', 2:'Papel', 3:'Tijeras'}
        self.input_machine=0
        self.score_M=0
        self.score_U=0
        self.game=0
    def lanzamiento(self, input_user):
        self.input_user=input_user
        self.input_machine=random.randint(1,3)
    def playGame(self):
        self.game+=1
        if (self.input_user==self.input_machine):
            return 'empate'
        elif (self.input_user==1 and self.input_machine == 3) or (self.input_user==2 and self.input_machine == 1) or (self.input_user==3 and self.input_machine == 2):
            self.score_U+=1
            return 'Ganaste !!! '
        else:
            self.score_M+=1
            return 'Perdiste contra la maquina !!!'
    def __str__(self):
        score=f'Puntuacion:\nUsuario: {self.score_U}\nMaquina: {self.score_M}'
        status_u=f'Elegiste: {self.estados[self.input_user]}\n'
        status_m=f'La maquina eligio: {self.estados[self.input_machine]}\n'
        return status_u+status_m+score

    

def main():
    print('Este es el juego de piedra papel o tijeras, para lanzar su estado siga los siguientes pasos\n')
    print("""             Piedra  => 1
             Papel   => 2
             Tijeras => 3""")
    opcion = int(input('Ingrese su opcion numerica: '))
    juego=Game()
    juego.lanzamiento(input_user=opcion)
    print(juego.playGame())
    print(juego)
if __name__ =='__main__':
    main()