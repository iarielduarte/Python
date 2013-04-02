def main():
	print "Ademas con python se puede hacer muchas cosas no solo script sin sentidos"
	print "Realmente si es tan bueno porque no tenemos buena documentacion de python"
	print "Este es un programa del sistema metrico"
	millas = input("Cuántas millas?: ")
	pies = input("Y cuántos pies?: ")
	pulgadas = input("Y cuántas pulgadas?: ")
	metros = 1609.344 * millas + 0.3048 * pies + 0.0254 * pulgadas
	print "La longitud es de ", metros, " metros"
main()