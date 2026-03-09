# Actividad #1 - Fundamentos de Python

## Convención de nombres

Se usa **snake_case** en todos los archivos.  
Todos los archivos siguen la estructura estándar:

```python
def main():
    pass

if __name__ == "__main__":
    main()
```

---

## Ejercicios

### Ejercicio 1 — Estructura de Estudiante (`ejercicio_1.py`)

Registra un estudiante con nombre, edad, estado, materias y notas. Calcula el promedio general, identifica la materia con mejor y peor nota, y determina si aprueba (promedio ≥ 3.0).

**Validaciones:**
- Mínimo 3 materias
- Notas en rango 0.0 a 5.0
- No se permiten materias duplicadas

```bash
python ejercicio_1.py
```

---

### Ejercicio 2 — Calculadora Monetaria (`ejercicio_2.py`)

Recibe un valor monetario y calcula:
- Impuesto del 19%
- Descuento del 10% si el valor base es ≥ 200.000 (si no, descuento 0)
- Total final = base + impuesto − descuento

```bash
python ejercicio_2.py
```

---

### Ejercicio 3 — Serie Fibonacci (`ejercicio_3.py`)

Recibe dos números enteros: el primero es el valor de inicio en la serie y el segundo es el número de iteraciones. Muestra la lista completa, cuántos términos se generaron y el último valor.

**Validaciones:**
- Las iteraciones no pueden ser negativas ni cero

```bash
python ejercicio_3.py
```

---

### Ejercicio 4 — Menú de Operaciones (`ejercicio_4.py`)

Presenta un menú con 3 opciones:

1. Verificar si un número es primo
2. Calcular el factorial de un número
3. Contar vocales en un texto (conteo individual por vocal)

```bash
python ejercicio_4.py
```

---

### Ejercicio 5 — Registro de Usuarios (`ejercicio_5.py`)

Solicita y valida nombre, edad y correo. Si algún dato es inválido, muestra un mensaje de error y vuelve a pedirlo. Al finalizar, muestra la lista de todos los usuarios registrados.

**Validaciones:**
- Nombre: mínimo 3 caracteres
- Edad: entre 0 y 120
- Correo: debe contener `@` y terminar en `.com` o `edu.co`

```bash
python ejercicio_5.py
```