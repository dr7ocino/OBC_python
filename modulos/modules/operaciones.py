class Operaciones :
    def __init__(self,number_a, number_b ):
        self.number_a=number_a
        self.number_b=number_b
        self._sum = 0
        self._resta=0
        self._multiplicacion=0
        self._division=0
    def suma(self):
        self._sum=self.number_a+self.number_b
        return 'La operacion suma es : {}'.format(self._sum)
    def resta(self):
        self._resta=self.number_a-self.number_b
        return 'La operacion resta es : {}'.format(self._resta)
    def multiplicacion(self):
        self._multiplicacion=self.number_a*self.number_b
        return 'La operacion multiplicacion es : {}'.format(self._multiplicacion)
    def division(self):
        self._division=self.number_a/self.number_b
        return 'La operacion division es : {}'.format(self._division)
