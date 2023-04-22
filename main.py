import math

print("** CALCULADORA CIENTÍFICA (BÁSICA) MAI2.0 **")

def sum(number1, number2):
	addition = number1 + number2
	print(f"""
        {number1}
       +{number2}
       ----------
        {addition}""")

def deduct(number1, number2):
	abstraction = number1 - number2
	print(f"""
        {number1}
       -{number2}
       ----------
        {abstraction}""")

def multiply(number1, number2):
	multiplication = number1 * number2
	print(f"""
        {number1}
       x{number2}
       ------------
        {multiplication}
       """)

def divide(number1, number2):
	division = number1 / number2
	rest = number1 % number2
	print(f"""
       {number1}/{number2}
       Total: {division}
       Resto: {rest}
       """)

def percentage_calc(number, percent):
	percentage = number * percent/100
	print(f"El {percent}% de {number} es \'{percentage}\'")

def raise_power(base, power):
	squared = pow(base, power)
	print(f"{number1}^{number2}={squared}")

def square_root(radicand):
	root = math.sqrt(radicand)
	print(f"2√{radicand}={root}")
 
def n_root(radicand, n):
	root = pow(radicand, 1/3)
	print(f"{n}√{radicand}={root}")

def calculator(func="", *args):
	return globals()[func](*args)


op = 0

while op != 9:
	print(
		"""
	1. Suma de 2 (dos) números
 	2. Resta de 2 (dos) números
	3. Multiplicación de 2 (dos) números
	4. División de 2 (dos) números
	5. Calcular el porcentaje
	6. Elevar 1 (un) número a la potencia indicada
 	7. Calcular la raíz cuadrada de 1 (un) número
	8. Calcular la raíz \'n\' de 1 (un) número
	9. Apagar la calculadora
 		"""
	)
	op = int(input("Tu opción: "))
	print("------------------------------------")
	if op == 1:
		number1 = float(input("1er operando: "))
		number2 = float(input("2do operando: "))
		calculator("sum", number1, number2)
	elif op == 2:
		number1 = float(input("1er operando: "))
		number2 = float(input("2do operando: "))
		calculator("deduct", number1, number2)
	elif op == 3:
		number1 = float(input("1er operando: "))
		number2 = float(input("2do operando: "))
		calculator("multiply", number1, number2)
	elif op == 4:
		number1 = float(input("1er operando: "))
		number2 = float(input("2do operando: "))
		calculator("divide", number1, number2)
	elif op == 5:
		number1 = float(input("Número al que quieres aplicar el porcentaje\n"))
		number2 = float(input("Valor del porcentaje: "))
		calculator("percentage_calc", number1, number2)
	elif op == 6:
		number1 = float(input("Valor de la base: "))
		number2 = int(input("Exponente: "))
		calculator("raise_power", number1, number2)
	elif op == 7:
		number = float(input("Valor del radicando: "))
		calculator("square_root", number)
	elif op == 8:
		number = float(input("Valor del radicando: "))
		n_number = int(input("Índice de la raíz: "))
		calculator("n_root", number, n_number)
	elif op == 9:
		print("** Apagando calculadora **")
		break
	else:
		print("Opción no válida")
	
