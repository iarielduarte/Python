"""
Autor Ariel Duarte
Fecha : 28/06/2015
Modulo para el Programa de Contactos telefonicos version 3
"""

#Creamos una funcion de bienvenida
def bienvenida():
    #Abrimos el archivo
    texto = open("../datos/archivos/archivo.txt","r")
    print(texto.read())
    print(">-----------------Menú Principal-------------<")
    print("Selecciona una opción:")
    print("1 - Agregar Contacto")
    print("2 - Listar Contacto")
    print("3 - Buscar Contacto")
    print("4 - Salir")
    print(">--------------------------------------------<")


#Creamos una funcion para escribir
def escribir():
    autoincremento = open("../datos/archivos/agenda2.csv",'r')
    
    
    for n in range(1,40):
        linea = autoincremento.readline()
        partido = linea.split(",")
        if partido[0]!="":
            memoria = partido[0]
    autoincremento.close()
    
    agenda = open("../datos/archivos/agenda2.csv",'a')
    identificador = 0
    identificador = int(memoria)+1
    nombre = input("Ingrese el nombre de contacto :")
    telefono = input("Ingrese telefono :")
    print("Se han guardado en la agenda el contacto: ",nombre,"con el telefono",telefono)
    agenda.write(str(identificador))
    agenda.write(",")
    agenda.write(nombre)
    agenda.write(",")
    agenda.write(telefono)
    agenda.write("\n")
    agenda.close()

#Creamos una funcion para listar
def listar(fin):
    lectura = open("../datos/archivos/agenda2.csv")
    print(">-----------------Lista de Contactos-------------<")
    print("\tId\t\tNombre\t\tTeléfono")
    print(">------------------------------------------------<")
    for i in range(0,fin):
        linea = lectura.readline()
        print(linea.replace(",","\t\t"))
        
    print(">------------------Fin de la lista---------------<")
    lectura.close()


#Creamos una de funcion de buscador
def buscador(nombre):
    lectura = open("../datos/archivos/agenda2.csv")
    for i in range(0,30):
        linea = lectura.readline()
        partido = linea.split(",")
        if nombre == partido[1]:
            print(">----------------Contacto Buscado---------------<")
            print("\t\tId : ",partido[0])
            print("\t\tNombre: ",partido[1])
            print("\t\tTeléfono: ",partido[2])
            print(">-----------------------------------------------<")
            break
    lectura.close()

#Creamos una de funcion de error
def error():
    print("La opción no es valida")
