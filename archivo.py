print('Hola Mundo')

def multiplicar(n1:int,n2:int) -> int:
    return n1 * n2

def main() -> None:
    opcion = input("Ingrese una opción: ")
    numero1 = int(input("Ingrese el primer numero:"))
    numero2 = int(input("Ingrese el segundo numero:"))
    if opcion == '+':
        sumar()
    elif opcion == '-':
        restar(numero7,numero4)
    elif opcion == '**':
        multiplicar(numero1,numero2)
    elif opcion == '/':
        dividir()
    else:
        print('Opción inválida')