print('Hola Mundo')

def sumar() -> int:
    num_a: int = int(input("Ingrese un numero: "))
    num_b: int = int(input("Ingrese otro numero"))
    return num_a + num_b

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
