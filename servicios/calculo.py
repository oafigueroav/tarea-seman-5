# rectangulo.py
# Clase para calcular el área de un rectángulo

class Rectangulo:
    """
    Clase que representa un rectángulo y permite calcular su área.
    """
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        """
        Método que calcula el área del rectángulo.
        Fórmula: área = base * altura
        """
        return self.base * self.altura

