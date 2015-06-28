"""
Autor Ariel Duarte
Fecha : 28/06/2015
Programa de Contactos telefonicos version 3
"""
import sys
import modulos_2

def principal():
   modulos_2.bienvenida()
   opcion = input("> ")
   print("Has seleccinado la opción", opcion)
   if opcion=="1":
      modulos_2.escribir()
      principal()
   elif opcion=="2":
       print("Ingrese cantidad de registos que quieres ver :")
       registros = input("> ")
       modulos_2.listar(int(registros))
       principal()
   elif opcion=="3":
      print("Ingrese el nombre a buscar")
      buscar = input("> ")
      modulos_2.buscador(buscar)
      principal()
   elif opcion=="4":
      sys.exit()
   else:
      modulos_2.error()
      principal()

#Llamar a la funcion principal
principal()
