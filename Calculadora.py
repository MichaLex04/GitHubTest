"""Funciones de la Calculadora:
JH Suma
JH Resta

JS Multiplicacion
JS Division

MLX Salida 2
"""# Programa en Python para multiplicación y división

print("=== Operaciones Matemáticas ===")

# Ingreso de datos
num1 = float(input(": 300"))
num2 = float(input("200: "))

# Proceso
multiplicacion = num1 * num2

if num2 != 0:
    division = num1 / num2
else:
    division = "No se puede dividir entre cero"

# Salida de resultados
print("Resultado de la multiplicación:", multiplicacion)
print("Resultado de la división:", division)