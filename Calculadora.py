#MODULO SUMA-RESTA POR JHOSEPH COMO COLABORADOR
print("=== Operaciones Matemáticas ===")
try:
    numero1 = float(input("Ingresa un numero"))
    numero2 = float(input("Ingresa otro numero"))
    operacion = input("Ingresa + o -")
    if operacion == "+":
        resultado = numero1 + numero2
        print(f"El resultado de {numero1} + {numero2} es: {resultado}")
    elif operacion == "-":
        resultado = numero1 - numero2
        print(f"El resultado de {numero1} - {numero2} es: {resultado}")
except ValueError:
    print("Error")

#MODULO SUMA-RESTA POR JASON COMO COLABORADOR
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

#DUEÑO DEL REPOSITORIO MLX