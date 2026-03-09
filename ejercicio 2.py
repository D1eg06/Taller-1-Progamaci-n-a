def main():
    valor_base = float(input("Ingrese el valor monetario: "))
    
    while valor_base < 0:
        print("ERROR: El valor no puede ser negativo. Intente de nuevo.")
        valor_base = float(input("Ingrese el valor monetario: "))
        
    else:
        def calcular_impuesto(valor_base):
            return valor_base * 0.19

        def calcular_descuento(valor_base):
            if valor_base >= 200000:
                return valor_base * 0.10
            else:
                return 0
        
        def calcular_total_final(valor_base, impuesto, descuento):
            return valor_base + impuesto - descuento

        impuesto = calcular_impuesto(valor_base)
        descuento = calcular_descuento(valor_base)
        total_final = calcular_total_final(valor_base, impuesto, descuento)

        print(f"\nValor base: {valor_base}")
        print(f"Impuesto (19%): {impuesto}")
        if descuento > 0:
            print(f"Descuento (10%): {descuento}")
        else:
            print("Descuento: 0 (no aplica)")
        print(f"Total final: {total_final}")
          
if __name__ == "__main__":
    main()