def main():
	print "Convierte medidas inglesas a sistema metrico"
	millas = input("Cu�ntas millas?: ")
	pies = input("Y cu�ntos pies?: ")
	pulgadas = input("Y cu�ntas pulgadas?: ")
	metros = 1609.344 * millas + 0.3048 * pies + 0.0254 * pulgadas
	print "La longitud es de ", metros, " metros"
main()