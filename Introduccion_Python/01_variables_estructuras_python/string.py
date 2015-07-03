'''
Created on 19/05/2012

@author: Willis Polanco
'''

def main():
    print("Trabajando con String:")
    valor = "Esto es un string de ejemplo"
    print(valor.upper())
    print(valor.lower())
    print(valor.capitalize())
    print(valor.swapcase())
    print(valor.find('u'))
    print(valor.replace('un', 'one'))
    print("    un ejemplo     ".strip())
    print("      otro ejemplo    ".rstrip())
    print("holamundo".isalnum())
    print("holatest".isalpha())
    print("2222ssss2".isdigit())
    print("una prueba".isprintable())
    
    texto = "Otro ejemplo de string {b} {a}".format(b=56, a=40)
    texto2 = "Otra forma de imprimir %d" %67
    print(texto)
    print(texto2)
    
    print(texto2.split("r"))
    print(", ".join(texto2.split()))
    
    
    
if __name__ == '__main__':
    main()