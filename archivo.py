print('Hola Mundo')

def sumar(n1: int, n2: int) -> int:
    return n1 + n2


def restar() -> None:
    numero_1 = input("Ingrese un numero: ")
    numero_2 = input("Ingrese otro numero: ")
    resta = numero_1 - numero_2
    print("El resultado de la resta es:", resta)


def multiplicar(n1: int, n2: int) -> int:
    return n1 * n2


def dividir(num1: int, num2: int) -> None:
    resultado: float = num1 / num2

    print(f'El resultado de la división entre {num1} y {num2} es: {resultado}')


def modulo(num1: int, num2: int) -> int:
    return num1 % num2

def main() -> None:
    opcion: str = input("Ingrese una opción: ")
    num1: int = int(input('Ingrese un número: '))
    num2: int = int(input('Ingrese otro número: '))

    if opcion == '+':
        sumar(num1, num2)
    elif opcion == '-':
        restar(num1, num2)
    elif opcion == '*':
        multiplicar(num1, num2)
    elif opcion == '/':
        dividir(num1, num2)
    elif opcion == '%':
        modulo(num1, num2)
    else:
        print('Opción inválida')
main()
