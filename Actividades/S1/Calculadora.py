suma = lambda a, b: a + b
resta = lambda a, b: a - b
division = lambda a, b: a / b
multiplicacion = lambda a, b: a * b
raizcuadrada = lambda a: a ** 0.5  

print("--- Calculadora ---")

numero1 = float(input("ingresa un numero: "))
numero2 = float(input("ingresa un numero: "))

print("\n--- Resultados ---")

print("El resultado de la suma es:", suma(numero1, numero2))
print("El resultado de la resta es:", resta(numero1, numero2))
print("El resultado de la división es:", division(numero1, numero2))
print("El resultado de la multiplicación es:", multiplicacion(numero1, numero2))
print("La raíz cuadrada del primer número es:", raizcuadrada(numero1))
