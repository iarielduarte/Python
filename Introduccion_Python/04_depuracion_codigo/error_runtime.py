
# -- En este ejemplo usaremos el Patron Model View Controller (MVC)

# -- CONTROLADOR -- 
class AccionAnimal:
    def ladrar(self): return self._hacerAlgo('ladrido')
    def vestir(self): return self._hacerAlgo('pelaje')
    def quack(self): return self._hacerAlgo('quack')
    def plumaje(self): return self._hacerAlgo('plumaje')

    def _hacerAlgo(self, accion):
        if accion in self.strings:
            return self.strings[accion]
        else:
            return 'El {} no tiene {}'.format(self.nombreAnimal(), accion)

    def nombreAnimal(self):
        return self.__class__.__name__.lower()

# -- MODELO -- 

class Pato(AccionAnimal):
    strings = dict(
        quack = "Quaaaaak!",
        plumaje = "El pato tiene plumas marrones y blancas."
    )
 
class Persona(AccionAnimal):
    strings = dict(
        ladrido = "La persona dice woof!",
        pelaje = "La persona usa un abrigo de piel.",
        quack = "La persona hace quack como un pato.",
        plumaje = "La persona toma una pluma del suelo y la coloca en su sombrero."
    )

class Perro(AccionAnimal):
    strings = dict(
        ladrido = "El perro rabioso hace Arf!",
        pelaje = "El perro tiene piel blanca con manchas marrones.",
    )

# -- VISTA -- 

def en_la_jaula(perro):
    print(perro.ladrar())
    print(perro.vestir())

def en_el_patio(pato):
    print(pato.quack())
    print(pato.plumaje())
 
def main():
    patico = Pato()
    maria = Persona()
    woofy = Perro()

    print("-- En el patio:")
    for o in ( patico, maria, woofy ):
        en_el_patio(o)

    print("-- En la jaula:")
    for o in ( patico, maria, woofy ):
        en_la_jaula(o)
 
if __name__ == "__main__": main()
