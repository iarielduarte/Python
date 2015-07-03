import sys
import time

__version__ = "1.1.0"

class numletras():
    """
        retornar un numero en letras,
        ej., 42 se convierte en "cuarenta-dos"
    """
    _letras = {
        'unidades': (
            'cero', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve'
        ), 'decenas': (
            '', 'diez', 'veinte', 'trenta', 'cuarenta', 'cincuenta', 'sesenta', 'setenta', 'ochenta', 'noventa'
        ), 'decimas': (
            'diez', 'once', 'doce', 'trece', 'catorce', 'quince', 'dieciseis', 'diecisite', 'dieciocho', 'diecinueve' 
        ), 'cuartos': (
            'en punto', 'un cuarto', 'media hora'
        ), 'rango': {
            'cientos': 'cientos'
        }, 'misc': {
            'menos': 'menos'
        }
    }
    _oor = 'OOR'    # Fuera de rango

    def __init__(self, n):
        self.__number = n;

    def numletras(self, num = None):
        "Retorna el numero como letras"
        n = self.__number if num is None else num
        s = ''
        if n < 0:           # numeros negativos
            s += self._letras['misc']['menos'] + ' '
            n = abs(n)
        if n < 10:          # numeros de un digito
            s += self._letras['unidades'][n]  
        elif n < 20:        # decimas
            s += self._letras['decimas'][n - 10]
        elif n < 100:       # decenas
            m = n % 10
            t = n // 10
            s += self._letras['decenas'][t]
            if m: s += '-' + numletras(m).numletras()    # resto
        elif n < 1000:      # cientos
            m = n % 100
            t = n // 100
            s += self._letras['unidades'][t] + ' ' + self._letras['rango']['cientos']
            if m: s += ' ' + numletras(m).numletras()    # resto
        else:
            s += self._oor
        return s

    def number(self):
        "Retorna el numero como numero"
        return str(self.__number);

class decirhora(numletras):
    """
        retorna la hora(a partir de dos parametros) como letras,
        ej., catorce para la medio dia, un cuarto pasado la una, etc.
    """

    _especiales = {
        'medio dia': 'medio dia',
        'media noche': 'media noche',
        'para': 'para la',
        'pasado la': 'pasado la'
    }

    def __init__(self, h, m):
        self._hora = abs(int(h))
        self._min = abs(int(m))

    def letras(self):
        h = self._hora
        m = self._min
        
        if h > 23: return self._oor     # error OOR 
        if m > 59: return self._oor

        sign = self._especiales['pasado la']        
        if self._min > 30:
            sign = self._especiales['para']
            h += 1
            m = 60 - m
        if h > 23: h -= 24
        elif h > 12: h -= 12

        # hword es la hora mundial)
        if h is 0: hword = self._especiales['media noche']
        elif h is 12: hword = self._especiales['medio dia']
        else: hword = self.numletras(h)

        if m is 0:
            if h in (0, 12): return hword   # para medio dia y media noche
            else: return "{} {}".format(self.numletras(h), self._letras['cuartos'][m])
        if m % 15 is 0:
            return "{} {} {}".format(self._letras['cuartos'][m // 15], sign, hword) 
        return "{} {} {}".format(self.numletras(m), sign, hword) 

    def digitos(self):
        "retorna la hora tradicional, ej., 13:42"
        return "{:02}:{:02}".format(self._hora, self._min)

class decirhora_t(decirhora):   # envoltura para que decirhora use objeto de tipo time
    """
        retorna la hora (a partir de objeto time) como letras
        ej, catorce para medio dia
    """
    def __init__(self, t):
        self._hora = t.tm_hour
        self._min = t.tm_min

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == 'prueba':
            prueba()
        else:
            try: print(decirhora(*(sys.argv[1].split(':'))).letras())
            except TypeError: print("Hora invalida ({})".format(sys.argv[1]))
    else:
        print(decirhora_t(time.localtime()).letras())

def prueba():
    print("\nprueba numeros:")
    lista = (
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 19, 20, 30, 
        50, 51, 52, 55, 59, 99, 100, 101, 112, 900, 999, 1000 
    )
    for l in lista:
        print(l, numletras(l).numletras())

    print("\nPrueba hora:")
    lista = (
        (0, 0), (0, 1), (11, 0), (12, 0), (13, 0), (12, 29), (12, 30),
        (12, 31), (12, 15), (12, 30), (12, 45), (11, 59), (23, 15), 
        (23, 59), (12, 59), (13, 59), (1, 60), (24, 0)
    )
    for l in lista:
        print(decirhora(*l).digitos(), decirhora(*l).letras())

    print("\nHora local es " + decirhora_t(time.localtime()).letras())

if __name__ == "__main__": main()
