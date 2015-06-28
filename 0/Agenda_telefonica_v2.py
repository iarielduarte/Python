"""
Autor Ariel Duarte
Fecha : 28/06/2015
Programa de Contactos telefonicos version 2
"""

import modulos

#Llamar a la funcion de bievenida
modulos.bienvenida()
    
opcion = input("> ")


print("Has seleccinado la opción", opcion)

if opcion=="1":
   modulos.escribir()
elif opcion=="2":
    print("Ingrese cantidad de registos que quieres ver :")
    registros = input("> ")
    modulos.listar(int(registros))
else:
   modulos.error()
