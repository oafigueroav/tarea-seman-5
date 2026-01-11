# Matriz 3x3 con valores numéricos
matriz = [
    [5, 8, 3],
    [2, 9, 4],
    [7, 1, 6]
]

def buscar_valor(matriz, valor_buscado):
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if matriz[fila][columna] == valor_buscado:
                return (fila, columna)
    return None

# Valor que deseas buscar
valor = int(input("Ingresa el valor que deseas buscar en la matriz: "))

# Ejecutar la búsqueda
resultado = buscar_valor(matriz, valor)

# Mostrar el resultado
if resultado:
    print(f"✅ Valor {valor} encontrado en la posición: fila {resultado[0]}, columna {resultado[1]}")
else:
    print(f"❌ Valor {valor} no se encontró en la matriz.")

