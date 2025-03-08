import unittest
from src.calculo_area import calcular_area_cuadrado

class TestCalculoArea(unittest.TestCase):
    def test_area_cuadrado(self):
        """Pruebas con valores positivos y cero."""
        self.assertEqual(calcular_area_cuadrado(4), 16)
        self.assertEqual(calcular_area_cuadrado(0), 0)
        self.assertEqual(calcular_area_cuadrado(2.5), 6.25)

    def test_valor_negativo(self):
        """Prueba para manejar valores negativos."""
        with self.assertRaises(ValueError):
            calcular_area_cuadrado(-1)

if __name__ == "__main__":
    unittest.main()
