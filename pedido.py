 # main.py
# Programa principal que utiliza la clase Circulo

from pedido import Circulo   # Importamos la clase desde el archivo circulo.py

def main():
    # Solicitar datos al usuario
    nombre_usuario: str = input("Ingrese su nombre: ")
    radio: float = float(input("Ingrese el radio del círculo en cm: "))

    # Crear objeto de la clase Circulo
    mi_circulo = Circulo(radio)

    # Calcular área
    area: float = mi_circulo.calcular_area()

    # Valor de referencia
    valor_referencia: int = 50

    # Comparación booleana
    es_mayor: bool = area > valor_referencia

    # Mostrar resultados
    print(f"\nHola {nombre_usuario}, el área del círculo con radio {radio} cm es: {area:.2f} cm²")

    if es_mayor:
        print(f"El área es mayor que {valor_referencia} cm² ✅")
    else:
        print(f"El área es menor o igual que {valor_referencia} cm² ❌")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
