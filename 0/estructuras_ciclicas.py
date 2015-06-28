"""
Autor Ariel Duarte
Fecha : 26/06/2015
Programa para lectura de archivos con While y For
"""
lectura = open("../datos/archivos/agenda2.csv")

#Bucle For
for i in range(0,25):
    print(lectura.readline())

print("Fin del archivo con For")

lectura.close()

#Bucle While
lectura = open("../datos/archivos/agenda2.csv")
numero = 0
while numero < 25:
    print(lectura.readline())
    numero = numero + 1

print("Fin del archivo con While")

lectura.close()






