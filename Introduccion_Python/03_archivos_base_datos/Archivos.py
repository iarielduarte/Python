'''
Created on 26/05/2012

@author: Willis Polanco
'''

def main():
    file = open("prueba.txt", "r")
    destino = open("nuevofile.txt", "w")
    for linea in file:
        print(linea, file=destino, end='')
    print("Termino la escritura..")
    
    
if __name__ == '__main__':
    main()