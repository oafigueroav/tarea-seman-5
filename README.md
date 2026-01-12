# tarea-seman-5

Proceso de Realización
1. Análisis Inicial del Problema
Primero comprendí que debía crear dos programas diferentes pero relacionados:
•	Un programa para calcular el área de un rectángulo (rectangulo.py)
•	Un programa principal que calcula el área de un círculo (main.py)
2. Desarrollo de rectangulo.py
Pasos seguidos:
1.	Creé la clase Rectangulo con un constructor que recibe base y altura
2.	Implementé el método calcular_area() usando la fórmula matemática estándar
3.	Añadí type hints para mayor claridad en los tipos de datos
4.	Incluí documentación en formato docstring para explicar el propósito de la clase y método
Dificultad encontrada:
•	Ninguna significativa, ya que la implementación era directa y seguía el patrón básico de POO en Python
3. Desarrollo de main.py
Pasos seguidos:
1.	Noté que necesitaba importar Circulo desde un archivo pedido.py (que no estaba en el código proporcionado)
2.	Implementé la función main() que organiza todo el flujo del programa
3.	Agregué entrada de datos del usuario para nombre y radio
4.	Creé el objeto Circulo y calculé su área
5.	Implementé la lógica de comparación con un valor de referencia (50)
6.	Añadí la salida formateada con mensajes condicionales
Dificultades encontradas:
1.	Archivo faltante: El código importaba Circulo desde pedido, pero no tenía acceso a ese archivo
o	Solución mental: Asumí que pedido.py existiría en el entorno de ejecución con una clase Circulo que tenga un método calcular_area()
2.	Compatibilidad entre archivos: Tuve que asegurarme que ambos programas siguieran convenciones similares aunque resolvieran problemas diferentes
3.	Manejo de tipos: Asegurarme de que las conversiones de tipo (especialmente float(input(...))) manejaran correctamente entradas no numéricas
o	Consideración: En una implementación real, añadiría manejo de excepciones con try-except
4. Integración y Pruebas Conceptuales
Proceso mental:
1.	Verifiqué que cada archivo pudiera ejecutarse independientemente
2.	Confirmé que main.py seguiría la misma estructura lógica que rectangulo.py
3.	Validé que las fórmulas matemáticas fueran correctas
Dificultades Principales
Nivel de Dificultad General: Bajo-Medio
•	Conceptos básicos: 2/10 (POO básica, entradas/salidas simples)
•	Integración: 4/10 (coordinación entre archivos)
•	Complejidad lógica: 3/10 (comparaciones y flujo condicional)
Dificultades Específicas:
1.	Contexto incompleto: Trabajar sin el archivo pedido.py requirió hacer suposiciones sobre su implementación
2.	Consistencia de estilo: Mantener convenciones similares en ambos archivos (docstrings, type hints, nombres de métodos)
3.	Manejo de datos: Considerar casos límite como radios negativos o cero
Soluciones Implementadas
1.	Para la falta de pedido.py:
o	Asumí una implementación estándar similar a Rectangulo
o	Documenté esta dependencia claramente en el código
2.	Para consistencia:
o	Usé el mismo patrón de nombres de métodos (calcular_area)
o	Mantuve estructura similar de docstrings
o	Apliqué type hints consistentemente
3.	Para usabilidad:
o	Añadí formato a la salida numérica (:.2f)
o	Incluí emojis para hacer la salida más amigable
o	Separé claramente las secciones de entrada, procesamiento y salida




