def main():

    def validar_materia(materia):
        if len(materia) < 3:
            print("ERROR: El nombre de la materia debe tener al menos 3 caracteres. Intente de nuevo.")
            return False
        return True

    def validar_nota(nota):
        if nota < 0.0 or nota > 5.0:
            print("ERROR: La nota debe estar entre 0.0 y 5.0. Intente de nuevo.")
            return False
        return True

    def obtener_materias_y_notas():
        materias = []
        notas = {}

        print("\nIngrese las materias y sus notas (mínimo 3).")
        while True:
            materia = input("Nombre de la materia (o 'fin' para terminar): ").strip()

            if materia.lower() == "fin":
                if len(materias) < 3:
                    print(f"ERROR: Debe ingresar al menos 3 materias. Lleva {len(materias)}.")
                    continue
                break

            if not validar_materia(materia):
                continue

            if materia in notas:
                print("ERROR: Esa materia ya fue ingresada.")
                continue

            while True:
                nota = float(input(f"Nota para '{materia}': "))
                if validar_nota(nota):
                    break
                else:
                    print("ERROR: Ingrese un número válido.")

            materias.append(materia)
            notas[materia] = nota

        return materias, notas

    def mostrar_informe(estudiante):
        notas = estudiante["notas"]
        promedio = sum(notas.values()) / len(notas)
        mejor = max(notas, key=notas.get)
        peor = min(notas, key=notas.get)
        aprueba = promedio >= 3.0

        print(f"  Informe del Estudiante")
        print(f"  Nombre  : {estudiante['nombre']}")
        print(f"  Edad    : {estudiante['edad']}")
        print(f"  Estado  : {estudiante['estado'].capitalize()}")
        print(f"\n  Notas por materia:")
        for materia, nota in estudiante["notas"].items():
            print(f"{materia}: {nota:.1f}")
        print(f"\n  Promedio general : {promedio:.2f}")
        print(f"  Mejor materia    : {mejor} ({notas[mejor]:.1f})")
        print(f"  Peor materia     : {peor} ({notas[peor]:.1f})")
        print(f"  Resultado        : {'APRUEBA' if aprueba else 'REPRUEBA'}")

    print("--- Registro de Estudiante ---")
    estudiante = {
        "nombre": input("Ingrese el nombre del estudiante: "),
        "edad": int(input("Ingrese la edad del estudiante: ")),
        "estado": input("Ingrese el estado (activo/inactivo): ").strip().lower(),
        "materias": [],
        "notas": {}
    }

    estudiante["materias"], estudiante["notas"] = obtener_materias_y_notas()

    mostrar_informe(estudiante)

if __name__ == "__main__":
    main()