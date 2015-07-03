'''
Created on 23/05/2012

@author: Willis Polanco
'''

class Animal:
    def comer(self):
        print("El animal esta comiendo")
    
    def caminar(self):
        print("El animal esta caminando")
        
    def hablar(self):
        print("El animal esta hablando")

class Perro(Animal):
    def __init__(self, raza='Chihuahua', color='Marron'):
        self.raza=raza
        self.color=color
        print(self.raza, self.color)
        
    def ladrar(self):
        print("Woof Woof")
        
    def caminar(self):
        print("Woofy esta caminando..")
        
    def comer(self):
        print("Woofy esta comiendo")
        
    def get_raza(self):
        return self.raza
    
    def set_raza(self, razanueva):
        self.raza = razanueva

class Gato(Animal):
    def caminar(self):
        print("Miau esta caminando...")
        
    def comer(self):
        print("Miau esta comiendo")

def main():
    Woofy = Perro("Pastor Aleman", "Pinto")
    Woofy.ladrar()
    Woofy.caminar()
    print(Woofy.get_raza())
    Woofy.set_raza("Raza Rara")
    print(Woofy.get_raza())
    
    Woofy.caminar()
    Woofy.comer()
    
    Gato1 = Gato()
    Gato1.comer()
    Gato1.caminar()
    
    for o in (Woofy, Gato1):
        o.comer()
        o.caminar()
        
    en_hogar(Gato1)
    en_parquecito(Woofy)
        
def en_hogar(lobito):
    print("Animal en el hogar:")
    lobito.comer()
    lobito.caminar()
    
def en_parquecito(gatito):
    print("Animal en el parquecito")
    gatito.comer()
    gatito.caminar()
        
    
    
if __name__ == '__main__':
    main()