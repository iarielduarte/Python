#Creamos una funcion de bienvenida
def bienvenida():
    #Abrimos el archivo
    texto = open("../datos/archivos/archivo.txt","r")
    print(texto.read())
    print(">-----------------Menú Principal-------------<")
    print("Selecciona una opción:")
    print("1 - Agregar Contacto")
    print("2 - Listar Contacto")
    print(">--------------------------------------------<")


#Creamos una funcion para escribir
def escribir():
    agenda = open("../datos/archivos/agenda2.csv",'a')
    identificador = input("Ingrese el ID :")
    nombre = input("Ingrese el nombre de contacto :")
    telefono = input("Ingrese telefono :")
    print("Se han guardado en la agenda el contacto: ",nombre,"con el telefono",telefono)
    agenda.write(identificador)
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

#Creamos una de funcion de error
def error():
    print("La opción no es valida")
