'''
Created on 26/05/2012

@author: Willis Polanco
'''

import sqlite3

def main():
    dbprueba = sqlite3.connect("dbprueba.db")
    dbprueba.execute("drop table if exists persona")
    dbprueba.execute("create table persona(nombre text, edad int)")
    dbprueba.execute("insert into persona(nombre, edad) values (?,?)", ("Juan", 23))
    dbprueba.execute("insert into persona(nombre, edad) values (?,?)", ("Miguel", 43))
    dbprueba.execute("insert into persona(nombre, edad) values (?,?)", ("Maria", 44))
    dbprueba.execute("insert into persona(nombre, edad) values (?,?)", ("Pedro", 14))
    dbprueba.execute("insert into persona(nombre, edad) values (?,?)", ("Marcos", 56))
    dbprueba.commit()
    
    cursor = dbprueba.execute("select nombre from persona order by nombre ")
    for fila in cursor:
        print(fila)

if __name__ == '__main__':
    main()