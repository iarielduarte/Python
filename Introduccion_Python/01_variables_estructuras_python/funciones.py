'''
Created on 18/05/2012

@author: Willis Polanco
'''


def main():
    print("Trabajando con funciones...")
    probarFuncion(4,7)
    funcion2(4, 2, 3,5,6,90.9, "hola")
    funcion3(3, 4, 5, 8, 9, 10, valor1 = "hola", valor2 = "mundo", valor3=100)
    print(funcionRetorno(2, 3, 4, 5, 6))
    for x in generarNum(0, 50, 1):
        print(x, end=' ')
    

def probarFuncion(i, j, k=59.9):
    print("Probando una funcion.", i, j, k)
    
def funcion2(i, j, k=23.44, *params):
    print("Probando otra funcion.", i, j, k, params)
    for x in params:
        print(x)

def funcion3(i, j, k, *lista, **argumentos):
    print(i, j, k, lista, argumentos)    
    for i in argumentos:
        print(i, argumentos[i])
    
def funcionRetorno(i, j, *tupla):
    return i * j * (tupla[0]+tupla[1] + tupla[2])

def generarNum(inicio, fin, incremento):
       x = inicio
       while(x<fin):
           yield x
           x = x+incremento

if __name__ == '__main__':
    main()