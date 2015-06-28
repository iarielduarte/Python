"""
Autor Ariel Duarte
Fecha : 26/06/2015
Programa para escritura y lectura de archivos planos
"""
#Abrimos el archivo
texto = open("../datos/archivos/archivo.txt","r")

#Leemos el contenido archivo
print(texto.read())

#Agenda
agenda = open("../datos/archivos/agenda.csv",'a')

#Borra todo el contenido archivo
#agenda.truncate()

nombre = input("Ingrese el nombre de contacto :")
telefono = input("Ingrese telefono :")

print("Se han guardado en la agenda el contacto: ",nombre,"con el telefono",telefono)


#Escribiendo el archivo
agenda.write(nombre)
agenda.write(",")
agenda.write(telefono)
agenda.write("\n")

agenda.close()

lectura = open("../datos/archivos/agenda.csv")


for i in range(0,6):
    print(lectura.readline())

print("Fin del archivo")


lectura.close()






