def main():
    def es_primo(numero):
        if numero < 2:
            return False
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                return False
        return True

    def calcular_factorial(numero):
        if numero < 0:
            return "ERROR: El número no puede ser negativo."
        elif numero == 0 or numero == 1:
            return 1
        else:
            factorial = 1
            for i in range(2, numero + 1):
                factorial *= i
            return factorial

    def contar_vocales(texto):
        vocales = "aeiou"
        conteo = {v: texto.count(v) for v in vocales}
        return conteo
    
    def mostrar_menu():
        print("Seleccione una operación")
        print("1. Determinar si un número es primo")
        print("2. Calcular factorial")
        print("3. Contar vocales en un texto")

        opcion = input("Ingrese el número de la operación que desea realizar: ")

        if opcion == "1":
            numero = int(input("Ingrese un número entero: "))
            if es_primo(numero):
                print(f"{numero} es un número primo.")
            else:
                print(f"{numero} no es un número primo.")
        
        elif opcion == "2":
            numero = int(input("Ingrese un número entero para calcular su factorial: "))
            resultado = calcular_factorial(numero)
            print(f"El factorial de {numero} es: {resultado}")
        
        elif opcion == "3":
            texto = input("Ingrese un texto para contar las vocales: ").lower()
            conteo_vocales = contar_vocales(texto)
            print("Conteo de vocales:")
            for vocal, conteo in conteo_vocales.items():
                print(f"{vocal}: {conteo}")
        
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 3.")
        
    mostrar_menu()
if __name__ == "__main__":
    main()