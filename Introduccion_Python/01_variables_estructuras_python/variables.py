print("Empezando a programar!")

# Definir variables tipo numericas
numero = float(100.76)
print(type(numero),numero)

# Definir variables tipo string
cadena = '''\
Nombre y Apellido
Edad, fecha Nacimiento
fecha ingreso, fecha retiro
'''
print(type(cadena), cadena)

otro = "Numero : {}".format(numero)
print(type(otro), otro) 

# Definir tipo de objetos tuplas

tupla = (4,5,6,7,8)
print(type(tupla), tupla)

# Definir tipo de objetos listas
listas = [1,3,5,6,8]
print(type(listas), listas)
listas.append(10)
listas.insert(0,0)
print(type(listas), listas)

texto = "Hoy es un dia bonito"
print(texto[4:9])

# Definir tipo de objetos Diccionarios
dic = dict( one =1, two =2, four=4, five="cinco")
for e in sorted(dic.keys()):
    print(e, dic[e])
    


