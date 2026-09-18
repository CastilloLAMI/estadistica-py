# Uso de git
#  Castillo Mamani Ivan Ramiro Código: 71936868 


def suma(a, b):
    # Retorna la suma de los dos parametros
    return a + b


def resta(a, b):
    # Retorna la resta de los dos parametros
    return a - b


def multiplicacion(a, b):
    # Retorna la multiplicacion de los dos parametros
    return a * b


def division(a, b):
    # Si el divisor es cero, retorna None para evitar el error
    if b == 0:
        return None
    return a / b


# ------------------------------------------------------------
# FUNCIÓN PRINCIPAL
# ------------------------------------------------------------

def leer_numero(mensaje):
    valor = input(mensaje)
    if valor.strip() == "":
        raise ValueError("Error: no puedes ingresar vacio.")
    return float(valor)


def main():
    print("=== CALCULADORA BASICA ===")

    # try-except: controla si el usuario escribe algo que no sea numero
    try:
        num1 = leer_numero("Ingrese el primer numero: ")
        num2 = leer_numero("Ingrese el segundo numero: ")
    except ValueError as e:
        if str(e) == "Error: no puedes ingresar vacio.":
            print(str(e))
        else:
            print("Error: debe ingresar valores numericos.")
        return

    # Menú de operaciones
    print("\nSeleccione una operacion:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")

    opcion = input("Opción (1-4): ")
    if opcion.strip() == "":
        print("Error: no puedes ingresar vacio.")
        return

    # Según la opción, se llama a la función correspondiente
    if opcion == "1":
        print("Resultaditoo:", suma(num1, num2))
    elif opcion == "2":
        print("Resultaditoo:", resta(num1, num2))
    elif opcion == "3":
        print("Resultaditoo:", multiplicacion(num1, num2))
    elif opcion == "4":
        # Control de división entre cero
        if num2 == 0:
            print("Error: no se puede dividir entre cero.")
        else:
            print("Resultaditoo:", division(num1, num2))
    else:
        # Opción que no existe
        print("Error: opcion no valida. Debe elegir entre 1 y 4.")


# ------------------------------------------------------------
# EJECUCIÓN
# Mejoras
# ------------------------------------------------------------

if __name__ == "__main__":
    main()