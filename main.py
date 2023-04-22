import math

print("** BIENVENID@ A TU CALCULADORA CIENTÍFICA **")

def sum(number1, number2):
	addition = number1 + number2
	return addition

def deduct(number1, number2):
	abstraction = number1 - number2
	return abstraction

def multiply(number1, number2):
	multiplication = number1 * number2
	return multiplication

def divide(number1, number2):
	division = number1 / number2
	return division

def raise_power(base, power):
	squared = pow(base, power)
	return squared

def root_extract(radicand):
	root = math.sqrt(radicand)
	return root

def calculator(func):
	return func()

number1 = float(input("Ingresa un número: "))
number2 = float(input("Ingresa otro número: "))

op = 0

while op != 9:
	print(
		"""
	1. Suma de 2 números
 	2. Resta de 2 números
	3. Multiplicación de 2 números
  4. División de 2 números
	5. Elevar 1 número a la potencia indicada
 	6. Sacar la raíz cuadrada de un número
	9. Apagar la calculadora
 		"""
	)
	if op == 1:
		
	

print(calculator())
