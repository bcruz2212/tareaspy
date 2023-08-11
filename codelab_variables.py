variable = "Entero"
variable += " "
variable += "Flotante"
variable += " "
variable += "booleanos"
variable += " "
variable += "cadenas"
variable += " " 
 # i.Concatena a la cadena las otras variables aplicando la conversión correcta para funcionar.
print(variable)

# ii. Investiga sobre el límite de los enteros y los flotantes en python y anotar sus descubrimientos como comentarios en el archivo
# Resp: En Python, los enteros no tienen límite de tamaño. El tipo de entero de Python3 no tiene límite de tamaño 
# y se puede usar como tipo largo. En cuanto a los flotantes, son representados en hardware de computadora como fracciones binarias en base 2. 
# Desafortunadamente, la mayoría de las fracciones decimales no pueden representarse exactamente como fracciones binarias. En general, los números de punto flotante decimal que ingresás en la computadora son sólo aproximados por los números de punto flotante binario que realmente se guardan en la máquina. En la mayoría de las máquinas hoy en día, los float se aproximan usando una fracción binaria con el numerador usando los primeros 53 bits con el bit más significativos y el denominador como una potencia de dos.

# iii. Formula suma
n = int(input("Porfavor ingresa un numero n: "))
suma_pares = int((n * (n+1))/2)
print("La suma de n es: " , suma_pares)
