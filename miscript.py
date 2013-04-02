def main():
	print "Convierte medidas inglesas a sistema metrico"
	millas = input("Cuántas millas?: ")
	pies = input("Y cuántos pies?: ")
	pulgadas = input("Y cuántas pulgadas?: ")
	metros = 1609.344 * millas + 0.3048 * pies + 0.0254 * pulgadas
	print "La longitud es de ", metros, " metros"
main()