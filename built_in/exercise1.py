####
class Paises:
    def __init__(self, list):
        self.paises=list
        self.sorted_countries=[]
    def changeOrder(self):
        self.sorted_countries=str(sorted(set(self.paises)))

    def __str__(self) -> str:
        return f'Paises=> {self.sorted_countries}, type=>{type(self.sorted_countries)}'

countries=input(f'Ingrese los paises separados por coma: ')
list_countries=countries.split(',')
sortCountries=Paises(list_countries)
sortCountries.changeOrder()
print(sortCountries)

