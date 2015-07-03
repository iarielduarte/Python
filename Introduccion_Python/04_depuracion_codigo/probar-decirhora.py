import decirhora
import unittest

class ProbarDecirHora(unittest.TestCase):
    def setUp(self):
        self.nums = list(range(11))

    def test_numbers(self):
        # Asegurar la conversion de numeros a letras correctamente
        letras = (
            'cero', 'uno', 'dos', 'tres', 'cuatro', 'cinco',
            'seis', 'siete', 'ocho', 'nueve', 'diez'
        )
        for i, n in enumerate(self.nums):
            self.assertEqual(decirhora.numletras(n).numletras(), letras[i])

    def test_time(self):
        tupla_horas = (
            (0, 0), (0, 1), (11, 0), (12, 0), (13, 0), (12, 29), (12, 30),
            (12, 31), (12, 15), (12, 30), (12, 45), (11, 59), (23, 15), 
            (23, 59), (12, 59), (13, 59), (1, 60), (24, 0)
        )
        letras_horas= (
            "media noche",
            "uno pasado la media noche",
            "once en punto",
            "medio dia",
            "uno en punto",
            "veinte-nueve pasado la medio dia",
            "media hora pasado la medio dia",
            "veinte-nueve para la uno",
            "un cuarto pasado la medio dia",
            "media hora pasado la medio dia",
            "un cuarto para la uno",
            "uno para la medio dia",
            "un cuarto pasado la once",
            "uno para la media noche",
            "uno para la uno",
            "uno para la dos",
            "OOR",
            "OOR"
        )
        for i, t in enumerate(tupla_horas):
            self.assertEqual(decirhora.decirhora(*t).letras(), letras_horas[i])

if __name__ == "__main__": unittest.main()
