'''
******************************************************
*** Programa para el proyecto calculo de comisiones***
*** Realizado por José Roberto Torres Bello        ***
*** Noviembre 2019                                 ***
****************************************************** 

Programa para calcular el monto real que quieres ganar al obtener clip
con la información de la pagina: https://clip.mx/costos-y-comisiones/

'''
iva=0.16 # IVA
ct=3.60/100 # Comision por transaccion

# Monto que en verdad quieres recibir
y=float(input("Ingresa el monto neto que quieres ganar: "))

# Si lo quieres a meses sin intereses, se hace un lower 
msi=input("¿Es con meses sin intereses? (Y/N): ")
msi=msi.lower()



# Si es a meses sin intereses
if msi == 'y':
	# Imprime en pantalla el plaza y seleccionalo
	print("3, 6, 9 12 meses")
	nmeses=int(input("¿A cuántos meses quieres pagar? "))
	print("Elegiste pago a "+str(nmeses)+" meses")

	# Porcentaje de comision dependiendo del plazo
	if nmeses==3:
		i=4.50/100
	elif nmeses==6:
		i=7.50/100	
	elif nmeses==9:
		i=9.90/100
	else:
		i=11.95/100

	# Calcula el monto neto a cobrar, aumentando las comisiones
	x=y/(1-ct-i-(ct+i)*iva)

	print("Monto a cobrar para obtener "+str(y)+" pesos:", x)

	# Si no le cobras la comision al cliente
	d=y*(1-ct-i-(ct+i)*iva)
	print("Si la comision no se la cobras al cliente obtienes: "+str(d))




# Si el pago no es a meses sin intereses	
else:
	print("Elegiste pago normal")

	x=y/(1-ct-ct*iva)
	print("Monto a cobrar para obtener "+str(y)+" pesos:", x)


	d=y*(1-ct-ct*iva)
	print("Si la comision no se la cobras al cliente obtienes: "+str(d))



