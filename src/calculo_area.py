"""
Módulo para calcular el área de un cuadrado.

Fórmula:
    A = a^2

Donde:
    A: Área del cuadrado
    a: Lado del cuadrado

Uso:
    area = calcular_area_cuadrado(5)
"""

def calcular_area_cuadrado(lado):
    """Calcula el área de un cuadrado."""
    if lado < 0:
        raise ValueError("El lado del cuadrado no puede ser negativo.")
    return lado ** 2

if __name__ == "__main__":
    lado = float(input("Ingrese el lado del cuadrado: "))
    print(f"El área del cuadrado es: {calcular_area_cuadrado(lado)}")
