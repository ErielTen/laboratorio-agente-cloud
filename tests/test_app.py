import unittest
from io import StringIO
from contextlib import redirect_stdout
from unittest.mock import patch

from app import main
from tasks import agregar_tarea


class TestApp(unittest.TestCase):
    def ejecutar_main(self, entradas, tareas_iniciales=None):
        salida = StringIO()
        with patch("builtins.input", side_effect=entradas), redirect_stdout(salida):
            main(tareas_iniciales=tareas_iniciales)
        return salida.getvalue()

    def test_ver_pendientes_con_tareas_precargadas(self):
        tareas = []
        agregar_tarea(tareas, "Estudiar agentes cloud", "Estudio")
        agregar_tarea(tareas, "Preparar laboratorio", "Trabajo")

        salida = self.ejecutar_main(["2", "3"], tareas)

        self.assertIn("- 1: Estudiar agentes cloud", salida)
        self.assertIn("- 2: Preparar laboratorio", salida)

    def test_agregar_tarea_desde_menu(self):
        salida = self.ejecutar_main(["1", "Comprar pan", "2", "3"])

        self.assertIn("Tarea agregada", salida)
        self.assertIn("- 1: Comprar pan", salida)

    def test_titulo_vacio_muestra_error_y_continua(self):
        salida = self.ejecutar_main(["1", "   ", "3"])

        self.assertIn("El titulo es obligatorio", salida)


if __name__ == "__main__":
    unittest.main()
