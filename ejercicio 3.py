def main():
    numero_1 = int(input("Ingrese el primer número entero (inicio): "))
    numero_2 = int(input("Ingrese el segundo número entero (número de iteraciones): "))

    while numero_2 < 0:
        print("ERROR: El número de iteraciones no puede ser negativo. Intente de nuevo.")
        numero_2 = int(input("Ingrese el segundo número entero (número de iteraciones): "))

    if numero_2 == 0:
        print("ERROR: El número de iteraciones debe ser mayor a 0. No se generó la serie.")
        return

    fibonacci_series = []
    a = 0
    b = 1

    while b < numero_1:
        a, b = b, a + b

    for _ in range(numero_2):
        fibonacci_series.append(b)
        a, b = b, a + b

    print(f"\nSerie Fibonacci generada: {fibonacci_series}")
    print(f"Número de términos generados: {len(fibonacci_series)}")
    print(f"Último valor incluido: {fibonacci_series[-1]}")

if __name__ == "__main__":
    main()