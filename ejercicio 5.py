def main():
    def validar_nombre(nombre):
        if len(nombre) < 3:
            print("ERROR: El nombre debe tener al menos 3 caracteres. Intente de nuevo.")
            return False
        return True

    def validar_edad(edad):
        if edad < 0 or edad > 120:
            print("ERROR: La edad debe estar entre 0 y 120. Intente de nuevo.")
            return False
        return True

    def validar_correo(correo):
        if "@" not in correo:
            print("ERROR: El correo debe contener '@'. Intente de nuevo.")
            return False
        if ".com" not in correo and "edu.co" not in correo:
            print("ERROR: El correo debe contener '.com' o 'edu.co'. Intente de nuevo.")
            return False
        return True
    
    def obtener_nombre():
        while True:
            nombre = input("Ingrese el nombre: ")
            if validar_nombre(nombre):
                return nombre

            
    def obtener_edad():
        while True:
            edad = int(input("Ingrese la edad: "))
            if validar_edad(edad):
                return edad

            
    def obtener_correo():
        while True:
            correo = input("Ingrese el correo: ").strip()
            if validar_correo(correo):
                return correo
      
                     
    usuarios = []
            
    def mostrar_lista(usuarios):
        print(f"---Lista de usuarios---")
        for i, usuario in enumerate(usuarios, 1):
            print(f"{usuario['nombre']} | Edad: {usuario['edad']} | {usuario['correo']}")

    while True:
        print("\n--- Registro de Usuario ---")
        nombre = obtener_nombre()
        edad = obtener_edad()
        correo = obtener_correo()
        usuarios.append({"nombre": nombre, "edad": edad, "correo": correo})
        
        continuar = input("¿Desea registrar otro usuario? (s/n): ").strip().lower()
        if continuar != 's':
            break
        
    mostrar_lista(usuarios)
    
if __name__ == "__main__":
    main()