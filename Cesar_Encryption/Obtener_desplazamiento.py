def obtener_desplazamiento():
    while True:
        try:
            n = int(input("Desplazamiento (entero positivo): ").strip())
            if n <= 0:
                print("¡Error! El desplazamiento debe ser un entero positivo")
                continue
            return n
        except ValueError:
            print("¡Error! Debe ingresar un número entero válido")