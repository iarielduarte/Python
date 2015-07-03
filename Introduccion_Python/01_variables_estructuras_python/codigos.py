'''
Created on 19/05/2012

@author: Willis Polanco
'''

def main():
#    naturales()
#    impares()
#    pares()
#    multiplo4()
#    sumaReverso()
#    suma()
#    producto()
#   capturaNumero()
#    sumaParImpar()
#    multiplo3()
    calculoPotencia()
    
def naturales():
###Programa que imprima los 25 primeros numeros naturales
    n = 1
    while n <= 25: 
        print(n)
        n += 1
    
def impares():
###Imprimir los numeros impares desde el 1 al 25, ambos inclusive
    n = 1
    h = ''
    while n <= 25:
        if n%2 != 0:
            h += ' %i' % n
        n += 1
        print(h)
        
def pares():
    ###Imprimir los numeros pares desde el 40 hasta el 60, ambos inclusive
    n = 40
    h = ''
    while n <= 60:
        if n%2 == 0:
            h += ' %i' % n
        n += 1
    print(h)

def multiplo4():
    ###Imprimir los numeros 48, 52, 56, ..., 120
    n = 48
    h = ''
    while n <= 120:
        h += ' %i' % n
        n += 4
    print(h)
    
def sumaReverso():
    ###Calcular e imprimir la suma 1+2+3+4+5+...+50
    n = 100
    h = ''
    while n >= 20:
        h += ' %i' % n
        n -= 5
    print(h)
    
def suma():
    ###Calcular e imprimir la suma 1+2+3+4+5+...+50
    h = range(1, 51)
    print(sum(h)) #con el comando sum se suma los numeros de una lista
    
def producto():
    ###Calcular e imprimir el producto 1*2*3*4*5*...*20
    n = 1
    h = 1
    while n <= 20:
        h *= n
        n += 1
    print(h)
    
def capturaNumero():
    ### Introducir un nuumero por teclado y decir si es par o impar
    h = int(input('Introduzca un numero: '))
    if h%2 == 0:
        print('Este numero es par')
    else:
        print('Este numero es impar')
    
def sumaParImpar():
##Imprimir los numeros del 1 al 100 y calcular la suma de todos los nuumeros 
###pares por un lado, y por otro, la de los impares.
    n = 1
    p = 0
    i = 0
    while n <= 100:
        print(n)
        if n%2 == 0:
            p += n
        else:
            i += n
        n += 1
    print ('\nLa suma de los pares es igual a %i' % p)
    print ('La suma de los impares es igual a %i' % i)  
    
def multiplo3():
    ### Imprimir y contar los numeros multiplos de 3 que hay entre 1 y 100.
    n = 1
    h = 0
    while n < 100:
        if n%3 == 0:
            print(n)
            h += 1
        n += 1
    print ('\nEntre 1 y 100 hay %i numeros multiplos de 3' % h)  
    
def calculoPotencia():
    ##Introducir dos valores A y B:
###Si A>=B, calcular e imprimir la suma 10+14+18+...+50 
###Si A/B<=30, calcular e imprimir el valor de (A^2+B^2)
    a = int(input('Primer valor: '))
    b = int(input('Segundo valor: '))
    n = 10
    suma = 0
    sumas = 0
    if a >= b:
        while n <= 50:
            suma += n
            n += 4
        print (suma)
    if a/b <= 30:
        sumas = (a**2+b**2)
        print (sumas)

if __name__ == '__main__':
    main()