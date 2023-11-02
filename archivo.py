print('Hola Mundo')

def main() -> None:
    opcion = input("Ingrese una opción: ")

    if opcion == '+':
        sumar()
    elif opcion == '-':
        restar()
    elif opcion == '*':
        multiplicar()
    elif opcion == '/':
        dividir()
    else:
        print('Opción inválida')