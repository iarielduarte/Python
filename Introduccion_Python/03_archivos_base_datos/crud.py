import sqlite3

def insertar(db, fila):
    db.execute('insert into persona (nombre, edad) values (?, ?)', (fila['nombre'], fila['edad']))
    db.commit()

def extraer(db, nombre):
    cursor = db.execute('select * from persona where nombre = ?', (nombre,))
    return cursor.fetchone()

def actualizar(db, fila):
    db.execute('update persona set edad = ? where nombre = ?', (fila['edad'], fila['nombre']))
    db.commit()

def borrar(db, nombre):
    db.execute('delete from persona where nombre = ?', (nombre,))
    db.commit()

def mostrar_filas(db):
    cursor = db.execute('select * from persona order by nombre')
    for filas in cursor:
        print('  {}: {}'.format(filas['nombre'], filas['edad']))

def main():
    db = sqlite3.connect('pruebadb.db')
    db.row_factory = sqlite3.Row
    print('Crear tabla persona')
    db.execute('drop table if exists persona')
    db.execute('create table persona ( nombre text, edad int )')

    print('Crear filas')
    insertar(db, dict(nombre = 'Juan', edad = 11))
    insertar(db, dict(nombre = 'Pedro', edad = 22))
    insertar(db, dict(nombre = 'Alex', edad = 43))
    insertar(db, dict(nombre = 'Hector', edad = 46))
    mostrar_filas(db)

    print('Extraer filas')
    print(dict(extraer(db, 'Juan')), dict(extraer(db, 'Pedro')))

    print('Actualizar filas')
    actualizar(db, dict(nombre = 'Juan', edad = 47))
    actualizar(db, dict(nombre = 'Alex', edad = 103))
    mostrar_filas(db)

    print('Borrar filas')
    borrar(db, 'Juan')
    borrar(db, 'Alex')
    mostrar_filas(db)

if __name__ == "__main__": main()
