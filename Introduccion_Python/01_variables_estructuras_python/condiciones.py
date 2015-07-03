'''
Created on 15/05/2012

@author: Willis Polanco
'''
def main():
    
    a,b,c = 6,3,8
    if a<b:
        print("{} Es menor que {}".format(a,b))
    elif a>b:
        print("{} Es mayor que {}".format(a,b))
    elif a==b:
        print("{} Es Igual que {}".format(a,b))
    else: 
        print("{} No es menor que {}".format(a,b))
    
    dias = dict(
                dia1 = "lunes", dia2="martes", dia3="miercoles", dia4="jueves", dia5="viernes"
                
            )
    
    miDia = "dia4"
    print(dias[miDia])
    
    var = "A es mayor que B" if a>b else "A no es mayor que B"
    print(var)
    
   
if __name__ == '__main__': main()
   