class rango_inclusive:
    def __init__(self, *args):
        numargs = len(args)
        if numargs < 1: raise TypeError('Requiere al menos un argumento')
        elif numargs == 1:
            self.inicio = 0
            self.fin = args[0]
            self.paso = 1
        elif numargs == 2:
            (self.inicio, self.fin) = args
            self.paso = 1
        elif numargs == 3:
            (self.inicio, self.fin, self.paso) = args
        else: raise TypeError('RangoIncluvise esperaba al menos  3 argumentos, tiene solo {}'.format(numargs))

    def __iter__(self):
        i = self.inicio
        while i <= self.fin:
            yield i
            i += self.paso

def main():
    o = rango_inclusive(4, 25, 3)
    for i in o: print(i, end = ' ')

if __name__ == "__main__": main()
