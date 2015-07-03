'''
Created on 21/05/2012

@author: Willis Polanco
'''
def main():
    print("Contenedores en Python.")
    tupla = (1,2,3,4,5)
    tupla2 = 6,
    tupla3 = tuple(range(20))
    print(tupla)
    print(tupla3)
    print(len(tupla3))
    print(min(tupla))
    print(max(tupla))
    
    lista = [3,4,5,6,7,8]
    listax = list(range(50))
    lista2 = [9,10,11]
    print(lista)
    print(len(lista))
    print(len(lista2))
    print(min(lista2))
    print(max(lista2))
    
    
    for x in lista:
        print(x)
        
    print(11 not in lista)
    lista.extend(range(10))
    print(lista)
    lista.insert(0, 1000)
    print(lista)
    lista.remove(1)
    print(lista)
    print(lista.pop(9))
    print(lista)
    print(lista.count(5))
    print(lista.index(5))
    print(listax)
    
    dic = {'uno':1, 'dos':2, 'tres':3}
    dic2 = dict(cuatro=4, cinco=5)
    dic3 = dict(seis=6, siete=7, **dic2)
    print(dic)
    print(dic2)
    print(dic3)
    
    for i, d in dic3.items():
        print(i,d)
        
    print('seis' in dic3)    
    print(dic2.get('cuatro'))
    print(dic2)
    print(dic2.pop('cuatro'))
    print(dic2)
    del dic3['seis']
    print(dic3)
    
if __name__ == '__main__':  main()