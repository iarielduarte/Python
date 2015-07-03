'''
Created on 15/05/2012

@author: Willis Polanco
'''

def main():
    
    # Definir ciclo usando while
    x=1
    while(x<200):
        if(x%3==0):
            print(x)
        x+= 1
    
    # Definir ciclo usando for
    print("Usando For: \n")
    for i in range(1,200):
        if(i%3==0):
            print(i)

    cadena = "Codiar es divertido"
    for i,c in enumerate(cadena):
        print(i,c)
        
    for c in cadena:
        if(c=='r'): continue
        print(c, end=' ')  
    else:
        print("\n Imprimir la parte else..")      

if __name__ == '__main__': main()
    