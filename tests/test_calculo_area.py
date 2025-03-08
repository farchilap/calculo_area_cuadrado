import unittest  # Importamos el módulo de pruebas unitarias Python
from src.calculo_area import calcular_area_cuadrado  # Importamos la función a probar

class TestCalculoArea(unittest.TestCase):

    """Clase de pruebas para la función calcular_area_cuadrado.
    Contiene pruebas tanto para casos exitosos como para casos donde la función debe fallar.
    """

    def test_area_cuadrado_exitoso(self):
        """Prueba casos donde la función debe devolver un resultado correcto.
        Se prueban diferentes valores de entrada y salida por si acaso.
        """
        # Caso donde el lado es un número entero positivo
        self.assertEqual(calcular_area_cuadrado(4), 16)  # 4 * 4 = 16
        
        # Caso donde el lado es cero (el área debe ser 0)
        self.assertEqual(calcular_area_cuadrado(0), 0)  # 0 * 0 = 0
        
        # Caso donde el lado es un número decimal positivo
        self.assertEqual(calcular_area_cuadrado(2.5), 6.25)  # 2.5 * 2.5 = 6.25

    def test_area_cuadrado_falla(self):
        """
        Prueba casos donde la función debe fallar y generar errores si en dado caso hubieran.
        Se verifican entradas no válidas como números negativos y texto.
        """
        # Caso donde el lado es negativo (debe generar un ValueError)
        with self.assertRaises(ValueError):
            calcular_area_cuadrado(-5)  # No se puede calcular el área de un cuadrado con lado negativo

        # Caso donde el lado es un texto en lugar de un número debe generar un error
        with self.assertRaises(TypeError):
            calcular_area_cuadrado("texto")  # No se puede calcular el área con una cadena de texto


if __name__ == "__main__":
    unittest.main()
